from flask import Blueprint

cat_app = Blueprint(
    "cat_app",
    __name__,
    url_prefix="/cat",
)


@cat_app.route("/")
def get_cats():
    return {"cats": "here"}