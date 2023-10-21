from .models.user import User
from .models.file import File
from .models.role import Role
from .base import Base
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(model_class=Base)


def get_db_connection():
    return db


def create_database(app):
    db.init_app(app)

    with app.app_context():
        db.create_all()

        obj = db.session.execute(
            db.select(User).where(User.role == Role.ADMIN)
        ).scalar()
        # ___________________________________________________________________________
        if not obj:
            obj = User(
                name="ivan",
                surname="ivanov",
                email="ivan@ivanov.ru",
                password="ivan",
                role=Role.ADMIN,
            )
            db.session.add(obj)
            db.session.commit()
            obj = obj.to_json()
            print("_______________________________________________")
            print("ADMIN entity created")
            print("login: ivan@ivanov.ru")
            print("password: ivan")
            print("_______________________________________________")
