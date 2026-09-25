import requests


API_URL = "https://jsonplaceholder.typicode.com/users"


def get_users():
    try:
        response = requests.get(API_URL, timeout=5)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print("خطا در اتصال به API:", e)
        return None