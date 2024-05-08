from flask import Blueprint
from flask import request
from . import crud

from models import Cat
from cat_user_api import get_name_cat


cat_app = Blueprint(
    "cat_app",
    __name__,
    url_prefix="/cat",
)


@cat_app.route("/")
def get_all_cats():
    cats =  crud.get_all_cats()
    return [str(cat.name) for cat in cats]


@cat_app.route("/create/")
def create_cat():
    name_cat = get_name_cat()
    crud.create_cat_user(cat_name=get_name_cat())
    return name_cat

    
    
@cat_app.route("/<int:cat_id>/")
def get_cat_by_id(cat_id: int):
    return Cat.query.get_or_404(
        cat_id,
        "not this cat"
        )
    
    