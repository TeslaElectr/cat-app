from flask import Blueprint

from . import crud

from cat_api import get_random_cats_fact

from models import Phrase


ph_app = Blueprint(
    "ph_app",
    __name__,
    url_prefix="/phrase",
)

@ph_app.route("/", methods=["GET"])
def ph_hello_page():
    return "<h1> ph_app_page </h1>"


@ph_app.route("/phrases/", methods=["GET"])
def get_all_phrases() -> list[Phrase]:
    return crud.get_list_of_phrases()

    
    
@ph_app.route("/<int:phrase_id>/", methods=["GET"])
def get_phrase_by_id(phrase_id: int) -> Phrase:
    return crud.get_phrase_by_id(phrase_id=phrase_id)

    
    
@ph_app.route("/create/")
def create_phrase_fact():
    fact = get_random_cats_fact()
    return f"<h1> Phrase: - {fact} </h1>"

    # new_frase = crud.create_phrase(
    #     phras=fact,
    #     )
    # return crud.get_phrase_by_id(phrase_id=new_frase.id)


    