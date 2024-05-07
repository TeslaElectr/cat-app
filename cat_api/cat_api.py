import requests
import cat_api_config




def get_random_cats_fact(url: str) -> str:
    responce = requests.get(
        url= cat_api_config.CAT_API_URL
        )

    return responce.json()['fact']