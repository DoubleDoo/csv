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
            db.create_all()