import jwt
from functools import wraps
from flask import jsonify
from flask import request
from app.database.methods.user import (
    db_get_user_for_auth,
    db_check_user_password,
    db_get_user_by_id,
)
import jwt
from flask import current_app, make_response
from flask import request, jsonify, current_app
from werkzeug.exceptions import Forbidden
from app.database.models.role import Role
from werkzeug import exceptions


def auth_guard(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        auth_headers = request.headers.get("Authorization", "").split()

        if len(auth_headers) != 2:
            raise exceptions.Unauthorized(f"Invalid token")

        try:
            token = auth_headers[1]
            data = jwt.decode(
                token,
                current_app.config["SECRET_KEY"],
                algorithms=[current_app.config["JWT_ALGORITHM"]],
            )
            user = db_get_user_by_id(data["user"]["id"])
        except jwt.ExpiredSignatureError:
            raise exceptions.Unauthorized(f"Expired")
        except jwt.InvalidTokenError:
            raise exceptions.Unauthorized(f"Invalid token")
        except Exception as e:
            print(e)
            raise exceptions.InternalServerError("Something went wrong")
        return f(user, *args, **kwargs)

    return _verify


def user_guard(f):
    @wraps(f)
    def _owner(user, *args, **kwargs):
        if user.role != Role.ADMIN and str(user.id) != str(id):
            raise exceptions.Unauthorized(f"Forbidden, owner only")
        return f(id, *args, **kwargs)

    return _owner


def admin_guard(f):
    @wraps(f)
    def _admin(user, *args, **kwargs):
        if user.role != Role.ADMIN:
            raise exceptions.Unauthorized(f"Forbidden, admin/owner only")
        return f(*args, **kwargs)

    return _admin


def delete_guard(f):
    @wraps(f)
    def _delete(user, *args, **kwargs):
        if user.role != Role.ADMIN and request.method == "DELETE":
            raise exceptions.Unauthorized(f"Forbidden, admin/owner only")
        return f(*args, **kwargs)

    return _delete
