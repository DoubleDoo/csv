import os


class Config:
    PROJECT = "app"
    SQLALCHEMY_DATABASE_URI = f'postgresql://{os.getenv("POSTGRES_USER")}:{os.getenv("POSTGRES_PASSWORD")}@{os.getenv("DB_HOST")}/{os.getenv("POSTGRES_DB")}'
    SECRET_KEY = os.getenv("SECRET_KEY")
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
    UPLOAD_FOLDER = "/app/files"
    ALLOWED_EXTENSIONS = {"csv"}
    SWAGGER_URL = os.getenv("SWAGGER_URL")
    API_URL = "/"
