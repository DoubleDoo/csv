from flask import Blueprint
from flask import jsonify
from flask import request
from app.database.methods.user import (
    db_create_user,
    db_get_user_by_id,
    db_get_all_users,
    db_delete_user_by_id,
    db_update_user_by_id,
    db_update_user_password,
)
from flask import Blueprint
from flask import jsonify
from flask import request
from app.auth.guards import auth_guard, admin_guard, user_guard, delete_guard

user = Blueprint("user", __name__, url_prefix="/user")


@user.route(f"/", methods=["GET"])
@auth_guard
@admin_guard
def get_all_users():
    objs = db_get_all_users()
    objs = [obj.to_json() for obj in objs]
    return jsonify(objs), 200


@user.route(f"/", methods=["POST"])
@auth_guard
@admin_guard
def create_user():
    jsn = request.get_json()
    data = {}
    data["name"] = jsn.get("name")
    data["surname"] = jsn.get("surname")
    data["email"] = jsn.get("email")
    data["password"] = jsn.get("password")
    obj = db_create_user(data)
    return jsonify(obj.to_json()), 201


@user.route(f"/<id>", methods=["GET"])
@auth_guard
@user_guard
def get_user(id):
    obj = db_get_user_by_id(id)
    return jsonify(obj.to_json()), 200


@user.route(f"/<id>", methods=["DELETE"])
@auth_guard
@delete_guard
def delete_user(id):
    db_delete_user_by_id(id)
    return "Deleted", 200


@user.route(f"/<id>", methods=["PUT"])
@auth_guard
@user_guard
def update_user(id):
    jsn = request.get_json()
    data = {}
    data["name"] = jsn.get("name")
    data["surname"] = jsn.get("surname")
    data["email"] = jsn.get("email")
    obj = db_update_user_by_id(id, data)
    return jsonify(obj.to_json()), 200


@user.route(f"/<id>", methods=["PUT"])
@auth_guard
@user_guard
def update_user_password(id):
    jsn = request.get_json()
    data = {}
    data["newPassword"] = jsn.get("newPassword")
    data["oldPassword"] = jsn.get("oldPassword")
    db_update_user_password(id, data)
    return jsonify("Done"), 200
