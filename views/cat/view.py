from flask import Blueprint
from flask import request
from . import crud

# from cat_api import get_random_cats_fact

from models import Phrase


# cat_app = Blueprint(
#     "cat_app",
#     __name__,
#     url_prefix="/cat",
# )