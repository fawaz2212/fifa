import requests

API_TOKEN = "ac3f9df41b9e4d37a2fe2f1320bd5e0b"

def get_live_matches():
    url = "https://api.football-data.org/v4/competitions/WC/matches"

    headers = {
        "X-Auth-Token": API_TOKEN
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json().get("matches", [])

    return []