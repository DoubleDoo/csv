from flask import Blueprint
from flask import jsonify
from app.database.methods.role import db_get_all_roles
from app.auth.guards import auth_guard, admin_guard, user_guard, delete_guard

role = Blueprint("role", __name__, url_prefix="/role")


@role.route("/")
@auth_guard
def index(user):
    return jsonify(db_get_all_roles())
