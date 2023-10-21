import uuid
from typing import List
from flask import jsonify
from numpy import int64
from sqlalchemy import BigInteger, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from ..base import Base
from sqlalchemy.dialects.postgresql import UUID, BIGINT, ARRAY, JSON


class File(Base):
    __tablename__ = "file"
    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(String)
    rows: Mapped[int] = mapped_column(Integer)
    columns = mapped_column(JSON)
    types = mapped_column(JSON)

    def __init__(self, name, columns, types, rows, id=""):
        if(id!=""):
           self.id = id 
        self.name = name
        self.columns = columns
        self.types = types
        self.rows = rows

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "rows": self.rows,
            "columns": self.columns,
            "types": self.types,
        }
