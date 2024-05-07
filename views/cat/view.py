from flask import Blueprint
from . import crud

cat_app = Blueprint(
    "cat_app",
    __name__,
    url_prefix="/cat",
)


@cat_app.route("/phrases", methods=["GET"])
def get_all_phrases():
    return crud.get_list_of_phrases()

    
