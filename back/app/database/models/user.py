import uuid
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from ..base import Base
from sqlalchemy.dialects.postgresql import UUID
from .role import Role
from werkzeug.security import generate_password_hash


class User(Base):
    __tablename__ = "user"
    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(String)
    surname: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    salt: Mapped[str] = mapped_column(String)
    role: Mapped[str] = mapped_column(String, default=Role.USER)

    def __init__(self, name, surname, email, password, role=Role.USER):
        self.name = name
        self.surname = surname
        self.email = email
        self.salt = generate_password_hash(password)
        self.role = role

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "email": self.email,
            "role": self.role,
        }
