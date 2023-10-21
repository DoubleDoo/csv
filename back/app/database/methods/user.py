from sqlalchemy import ScalarResult
from ..models.user import User
from ..models.role import Role
from ..database import get_db_connection
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug import exceptions

db = get_db_connection()

entity_name = "user"


def db_create_user(data) -> User:
    obj = User(
        name=data["name"],
        surname=data["surname"],
        email=data["email"],
        password=data["password"],
    )
    try:
        db.session.add(obj)
        db.session.commit()
    except Exception as e:
        print(e)
        raise exceptions.Conflict(f"Database create {entity_name} error")
    return obj


def db_get_all_users() -> list[User]:
    try:
        objs: ScalarResult[User] = db.session.execute(db.select(User)).scalars()
    except Exception as e:
        print(e)
        raise exceptions.NotFound(f"Database get {entity_name} error")
    return objs


def db_get_user_by_id(id: str) -> User:
    try:
        obj: User = db.session.execute(db.select(User).where(User.id == id)).scalar()
    except Exception as e:
        print(e)
        raise exceptions.NotFound(f"Database get {entity_name} by id error")
    return obj


def db_update_user_by_id(id: str, data) -> User:
    obj = db_get_user_by_id(User, id)
    if data["name"]:
        obj.name = data["name"]
    if data["surname"]:
        obj.surname = data["surname"]
    if data["email"]:
        obj.email = data["email"]
    try:
        db.session.commit()
    except Exception as e:
        print(e)
        raise exceptions.Conflict(f"Database update {entity_name} error")
    return obj


def db_delete_user_by_id(id: str) -> None:
    obj = db_get_user_by_id(id)
    try:
        db.session.delete(obj)
        db.session.commit()
    except Exception as e:
        print(e)
        raise exceptions.Conflict(f"Database delete {entity_name} error")


def db_get_user_for_auth(data) -> User:
    try:
        obj: User = db.session.execute(
            db.select(User).where(User.email == data["email"])
        ).scalar()
    except Exception as e:
        print(e)
        raise exceptions.NotFound(f"User for auth not found")
    return obj


def db_check_user_password(usr_password: str, password: str) -> None:
    if not check_password_hash(usr_password, password):
        raise exceptions.Unauthorized(f"Wrong password")


def db_update_user_password(id: str, data) -> None:
    obj = db_get_user_by_id(User, id)
    if data["newPassword"] and data["oldPassword"]:
        db_check_user_password(obj.salt, data["oldPassword"])
        obj.salt = generate_password_hash(data["newPassword"])
    try:
        db.session.commit()
    except Exception as e:
        print(e)
        raise exceptions.Conflict(f"Database update user password error")
    return obj

def db_user_init() -> None:
    obj = db.session.execute(
            db.select(User).where(User.role == Role.ADMIN)
        ).scalar()
    if not obj:
        obj = User(
            name="admin",
            surname="admin",
            email="admin@admin.ru",
            password="admin",
            role=Role.ADMIN,
            )
        db.session.add(obj)
        db.session.commit()
            
    obj2 = db.session.execute(
        db.select(User).where(User.role == Role.USER)
    ).scalar()
    if not obj2:
        obj2 = User(
            name="user",
            surname="user",
            email="user@user.ru",
            password="user",
            role=Role.USER,
        )
        db.session.add(obj2)
        db.session.commit()