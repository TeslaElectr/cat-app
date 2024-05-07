import requests


url = "https://catfact.ninja/fact"
# from cat_api_config import CAT_API_URL as url

def get_random_cats_fact() -> str:
    responce = requests.get(
        url=url,
        )

    return responce.json()['fact']
    
    
if __name__ == "__main__":
    print(get_random_cats_fact())