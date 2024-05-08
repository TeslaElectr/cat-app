from flask import Blueprint
from flask import request
from flask import url_for
from flask import redirect
from flask import render_template
from . import crud

from models import Cat
from other_api import get_name_cat


cat_app = Blueprint(
    "cat_app",
    __name__,
    url_prefix="/cat",
)


@cat_app.route("/", endpoint="list")
def get_all_cats():
    cats =  crud.get_all_cats()
    return render_template(
        'cats/cat_list.html',
        cats = cats,
    )


@cat_app.route("/create/", endpoint="create")
def create_cat():
    cat = crud.create_cat_user(cat_name=get_name_cat())
    url = url_for("cat_app.detail", cat_id=cat.id)
    return redirect(url)

    
    
@cat_app.route("/<int:cat_id>/", endpoint="detail")
def get_cat_by_id(cat_id: int):
    cat = crud.get_cat_by_id(cat_id)

    return render_template(
        "cats/details.html",
        cat=cat,
    )