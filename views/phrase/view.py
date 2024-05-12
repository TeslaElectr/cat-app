from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for

from . import crud

from other_api import get_random_cats_fact

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
    
    
@ph_app.route("/<int:fact_id>/")
def get_phrase_by_id(fact_id: int) -> Phrase.str_phrase:
    fact = crud.get_phrase_by_id(phrase_id=fact_id)
    return "<h1> fact </h1>"
    
    
@ph_app.route("/create/<int:cat_id>/", endpoint="create")
def create_phrase_fact(cat_id: int):
    crud.create_phrase(
        phras=get_random_cats_fact(),
        cat_id=cat_id
        )

    url = url_for('cat_app.detail',cat_id=cat_id)

    return redirect(url)


    