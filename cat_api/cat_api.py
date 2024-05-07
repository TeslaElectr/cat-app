import requests


from .cat_api_config import CAT_API_URL


def get_random_cats_fact() -> str:
    responce = requests.get(
        url=CAT_API_URL
        )

    return responce.json()['fact']