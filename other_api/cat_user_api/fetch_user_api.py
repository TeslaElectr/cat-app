import requests


def get_json_user() -> str:
    USER_API_URL = "https://randomuser.me/api/"
    responce = requests.get(url=USER_API_URL)
    return responce 

    
def get_name_cat() -> str:
    name = get_json_user().json()
    return "{}_{}".format(
        name['results'][0]['name']['first'],
        name['results'][0]['name']['last']
    )


# def main():
#     print(get_name_cat())
#     return None
    

# if __name__ == "__main__":
#     main()
    

