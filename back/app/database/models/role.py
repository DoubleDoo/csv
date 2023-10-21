import enum


class Role(str, enum.Enum):
    ADMIN = "ADMIN"
    USER = "USER"

    def to_json(self):
        return [self.ADMIN, self.USER]
