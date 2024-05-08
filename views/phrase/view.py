from flask import Blueprint
from flask import render_template

from . import crud

from cat_api import get_random_cats_fact

from models import Phrase
from views.cat import crud as cat_crud


ph_app = Blueprint(
    "ph_app",
    __name__,
    url_prefix="/facts",
)

@ph_app.route(
    "/",
    endpoint='facts_page'
    )
def ph_hello_page():
    return render_template('phrases/home.html')


@ph_app.route(
    "/list/",
    endpoint="facts",
)
def get_all_phrases() -> list[Phrase]:
    phrases = crud.get_list_of_phrases()
    # return [str(phrase.str_phrase) for phrase in phrases]
    return render_template(
        'phrases/list_phrases.html',
        phrases=phrases,
    )
    
    
@ph_app.route("/<int:phrase_id>/")
def get_phrase_by_id(phrase_id: int) -> Phrase.str_phrase:
    fact = crud.get_phrase_by_id(phrase_id=phrase_id)
    return "<h1> fact </h1>"
    
    
@ph_app.route("/create/")
def create_phrase_fact():
    rnd_id = 1  # ---------------------------------------- the temporary solution
    get_random_cat = cat_crud.get_cat_by_id(cat_id=rnd_id)
    fact = get_random_cats_fact()
    crud.create_phrase(
        phras=fact,
        cat_id=get_random_cat.id,
        )

    return f"<h1> {fact} </h1>"


    