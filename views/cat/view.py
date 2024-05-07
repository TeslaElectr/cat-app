from flask import Blueprint
from flask import request
from . import crud

from models import Phrase


cat_app = Blueprint(
    "cat_app",
    __name__,
    url_prefix="/cat",
)


@cat_app.route("/phrases/", methods=["GET"])
def get_all_phrases() -> list[Phrase]:
    return crud.get_list_of_phrases()

    
    
@cat_app.route("/phrase/<int:phrase_id>/", methods=["GET"])
def get_phrase_by_id(phrase_id: int) -> Phrase:
    return crud.get_phrase_by_id(phrase_id=phrase_id)

    
    
@cat_app.route("/create-phrase/")
def create_phrase_fact():
    # fact = get_random_cats_fact()
    return "<h1> Phrase: - "

    # new_frase = crud.create_phrase(
    #     phras=fact,
    #     )
    # return crud.get_phrase_by_id(phrase_id=new_frase.id)


    
