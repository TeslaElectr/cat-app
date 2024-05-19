from flask import Blueprint
from flask import render_template


root_app = Blueprint(
    "root_app",
    __name__,
    url_prefix="/",
)


@root_app.route("/")
def hello_world():
    return render_template("base.html")
    
    