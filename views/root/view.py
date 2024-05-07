from flask import Blueprint


root_app = Blueprint(
    "root_app",
    __name__,
    url_prefix="/",
)


@root_app.route("/")
def hello_world():
    return "<h1> Hellow World! </h1>"
    
    