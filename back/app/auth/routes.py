from flask import Blueprint
from flask import jsonify
from flask import request
from app.database.methods.user import db_get_user_for_auth, db_check_user_password
from datetime import datetime
from datetime import timedelta
import jwt
from flask import current_app
from werkzeug import exceptions

auth = Blueprint("auth", __name__, url_prefix="/auth")


@auth.route("/", methods=["POST"])
def login():
    jsn = request.get_json()
    data = {}
    data["email"] = jsn.get("email")
    obj = db_get_user_for_auth(data)
    db_check_user_password(obj.salt, jsn.get("password"))
    token = jwt.encode(
        {
            "user": {
                "id": str(obj.id),
                "email": obj.email,
                "name": obj.name,
                "surname": obj.surname,
                "role": obj.role,
            },
            "exp": datetime.utcnow() + timedelta(minutes=360),
        },
        current_app.config["SECRET_KEY"],
        algorithm=current_app.config["JWT_ALGORITHM"],
    )
    return jsonify(
        {
            "token": token,
            "user": {
                "id": str(obj.id),
                "email": obj.email,
                "name": obj.name,
                "surname": obj.surname,
                "role": obj.role,
            },
        }
    )
