from flask import Blueprint
from flask import jsonify
from flask import request
import flask
from app.database.methods.file import (
    db_create_file,
    db_get_all_files,
    db_get_file_by_id,
    db_delete_file_by_id,
)
import os
import json
from flask import Blueprint
from flask import current_app
from flask import jsonify
from flask import request
from app.auth.guards import auth_guard, admin_guard, user_guard, delete_guard
from werkzeug.utils import secure_filename
from flask import current_app
import pandas as pd
import os
from werkzeug.utils import secure_filename
from werkzeug import exceptions
import uuid
import re

file = Blueprint("file", __name__, url_prefix="/file")


def allowed(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower()
        in current_app.config["ALLOWED_EXTENSIONS"]
    )


@file.route("/", methods=["POST"])
@auth_guard
def demo(user):
    id = uuid.uuid4()
    readchunks = True
    with open(f"{current_app.config['UPLOAD_FOLDER']}/{id}.csv", "bw") as f:
        chunk_size = 4096
        chunk = b""
        name = ""
        while bytes(chunk) != b"\r\n":
            chunk = flask.request.stream.readline()
            result = re.findall(r"filename=\".+\"", str(chunk, encoding="utf-8"))
            if len(result) > 0:
                name = result[0]
                name = name.split('"')[1]
        while readchunks:
            chunk = flask.request.stream.read(chunk_size)
            if len(chunk) == 0:
                readchunks = False
                f.close()
            else:
                f.write(chunk)
    filename = f"{current_app.config['UPLOAD_FOLDER']}/{id}.csv"
    df = pd.read_csv(filename, low_memory=False)
    print(df.info())
    data = {}
    data["id"] = id
    data["name"] = name
    data["columns"] = json.dumps(df.columns.tolist())
    data["types"] = json.dumps([str(tp) for tp in df.dtypes.values.tolist()])
    data["rows"] = df.shape[0]
    obj = db_create_file(data)
    return jsonify(obj.to_json()), 200


@file.route("/", methods=["GET"])
@auth_guard
def get_files(user):
    objs = db_get_all_files()
    objs = [obj.to_json() for obj in objs]
    return jsonify(objs), 200


@file.route("/<id>", methods=["DELETE"])
@auth_guard
@admin_guard
def delete_file_by_id(id):
    db_delete_file_by_id(id)
    os.remove(os.path.join(current_app.config["UPLOAD_FOLDER"], f"{id}.csv"))
    return "Deleted", 200


@file.route("/<id>", methods=["POST"])
def get_sorted_data_part(id):
    jsn = request.get_json()
    data = {}
    data["page"] = jsn.get("page")
    data["size"] = jsn.get("size")
    data["sort"] = jsn.get("sort")
    obj = db_get_file_by_id(id)
    print(data)
    file_path = os.path.join(current_app.config["UPLOAD_FOLDER"], f"{id}.csv")
    skip_rows = data["page"] * data["size"]
    dataframe = pd.read_csv(
        file_path,
        names=json.loads(obj.columns),
        iterator=True,
        header=None,
        skiprows=skip_rows+1,
        chunksize=data["size"],
        encoding="unicode_escape",
    )
    chunk = next(dataframe)
    if len(data["sort"])!=0:
        chunk = chunk.sort_values(by=[data["sort"][0]["column"]], ascending=(data["sort"][0]["dirrection"]=="ascend"))

    return (
        jsonify({"file": obj.to_json(), "data": chunk.to_json(orient="records")}),
        200,
    )
