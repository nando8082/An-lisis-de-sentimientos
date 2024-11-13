# services/twitter_service.py

import requests
from config import TWITTER_BEARER_TOKEN


def get_twitter_metrics(username):
    url = f"https://api.twitter.com/2/users/by/username/{
        username}?user.fields=public_metrics"
    headers = {"Authorization": f"Bearer {TWITTER_BEARER_TOKEN}"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        user_data = response.json()
        return user_data  # Esto incluye métricas como seguidores, tweets, etc.
    else:
        return {"error": "Failed to fetch Twitter data"}
