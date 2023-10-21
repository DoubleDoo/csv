from .models.user import User
from .models.file import File
from .models.role import Role
from .base import Base
from flask_sqlalchemy import SQLAlchemy
import time

db = SQLAlchemy(model_class=Base)


def get_db_connection():
    return db


def create_database(app):
    db.init_app(app)

    with app.app_context():
        tries = 5
        while tries > 0:
            try:
                db.create_all()
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
                    obj = obj.to_json()
                obj = db.session.execute(
                    db.select(User).where(User.role == Role.USER)
                ).scalar()
                if not obj:
                    obj = User(
                        name="user",
                        surname="user",
                        email="user@user.ru",
                        password="user",
                        role=Role.USER,
                    )
                    db.session.add(obj)
                    db.session.commit()
                    obj = obj.to_json()
                    tries = 0
            except:
                tries += -1
                print('Failed to create Database, ADMIN and USER. Waiting and then trying again (try countdown: %s)' % tries)
                time.sleep(5000)
        print("Base USER and ADMIN existed")
