from flask import Flask
from app.config import Config
from app.auth import auth
from app.role import role
from app.user import user
from app.file import file
from flask_swagger_ui import get_swaggerui_blueprint

def create_app():
    app = Flask(__name__, static_url_path="", static_folder="static")
    app.url_map.strict_slashes = False
    app.config.from_object(Config)
    app.register_blueprint(auth)
    app.register_blueprint(role)
    app.register_blueprint(user)
    app.register_blueprint(file)
    swagger_ui_blueprint = get_swaggerui_blueprint(
        app.config["SWAGGER_URL"],
        app.config["API_URL"],
        config={"app_name": "CSV App"}
        # oauth_config={
        #    'clientId': "your-client-id",
        #    'clientSecret': "your-client-secret-if-required",
        #    'realm': "your-realms",
        #    'appName': "your-app-name",
        #    'scopeSeparator': " ",
        #    'additionalQueryStringParams': {'test': "hello"}
        # }
    )
    app.register_blueprint(swagger_ui_blueprint)

    return app
