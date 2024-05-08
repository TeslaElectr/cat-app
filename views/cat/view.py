from flask import Blueprint
from flask import request
from . import crud

from models import Cat


cat_app = Blueprint(
    "cat_app",
    __name__,
    url_prefix="/cat",
)


@cat_app.route("/")
def get_all_cats():
    return crud.get_all_cats()


@cat_app.route("/create/")
def create_cat(cat_name: str):
    return crud.create_cat_user(cat_name=cat_name)
    