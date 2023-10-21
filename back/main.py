from app import create_app
from app.database import create_database
from werkzeug import exceptions

app = create_app()
create_database(app)


@app.after_request
def response_headers_cors(resp):
    resp.headers["Access-Control-Allow-Origin"] = "*"
    resp.headers["Access-Control-Allow-Methods"] = "*"
    resp.headers["Access-Control-Allow-Headers"] = "*"
    return resp


@app.route("/")
def index():
    return "CSV API"


@app.errorhandler(exceptions.NotFound)
def handle_not_found(e: exceptions):
    return e, 404


@app.errorhandler(exceptions.Unauthorized)
def handle_not_unauthorized(e: exceptions):
    return e, 401


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
