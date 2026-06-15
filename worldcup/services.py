import requests

API_TOKEN = "ac3f9df41b9e4d37a2fe2f1320bd5e0b"

def get_standings():
    url = "https://api.football-data.org/v4/competitions/WC/standings"

    headers = {
        "X-Auth-Token": API_TOKEN
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()

    return None

from datetime import date, timedelta
import requests

API_TOKEN = "ac3f9df41b9e4d37a2fe2f1320bd5e0b"

def get_live_matches():

    yesterday = date.today() - timedelta(days=1)
    tomorrow = date.today() + timedelta(days=1)

    url = (
        f"https://api.football-data.org/v4/matches"
        f"?dateFrom={yesterday}"
        f"&dateTo={tomorrow}"
    )

    headers = {
        "X-Auth-Token": API_TOKEN
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data.get("matches", [])

    return []