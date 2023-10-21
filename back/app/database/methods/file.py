from sqlalchemy import ScalarResult
from ..models.file import File
from ..database import get_db_connection
from werkzeug import exceptions

db = get_db_connection()

entity_name = "file"


def db_create_file(data) -> File:
    if data["id"]:
        obj = File(
            id=data["id"],
            name=data["name"],
            columns=data["columns"],
            types=data["types"],
            rows=data["rows"],
        )
    else:
        obj = File(
            name=data["name"],
            columns=data["columns"],
            types=data["types"],
            rows=data["rows"],
        )
    try:
        db.session.add(obj)
        db.session.commit()
    except Exception as e:
        print(e)
        raise exceptions.Conflict(f"Database create {entity_name} error")
    return obj


def db_get_all_files() -> list[File]:
    try:
        objs: ScalarResult[File] = db.session.execute(db.select(File)).scalars()
    except Exception as e:
        print(e)
        raise exceptions.NotFound(f"Database get {entity_name} error")
    return objs


def db_get_file_by_id(id) -> File:
    try:
        obj: File = db.session.execute(db.select(File).where(File.id == id)).scalar()
    except Exception as e:
        print(e)
        raise exceptions.NotFound(f"Database get {entity_name} by id error")
    return obj


def db_delete_file_by_id(id) -> None:
    obj = db_get_file_by_id(id)
    try:
        db.session.delete(obj)
        db.session.commit()
    except Exception as e:
        print(e)
        raise exceptions.Conflict(f"Database delete {entity_name} error")
