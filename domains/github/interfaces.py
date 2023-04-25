import json

import requests
from django.conf import settings


def exchange_code(code):
    params = {
        "client_id": settings.GITHUB_CLIENT_ID,
        "client_secret": settings.GITHUB_CLIENT_SECRET,
        "code": code,
    }
    url = "https://github.com/login/oauth/access_token"
    headers = {"Accept": "application/json"}
    response = requests.post(url, data=params, headers=headers)

    return parse_response(response)


def parse_response(response):
    if response.status_code == 200:
        return response.json()
    print(response)
    print(response.text)
    return {}


def user_info(token):
    uri = "https://api.github.com/user"

    auth = f"Bearer {token}"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": auth,
    }

    response = requests.get(uri, headers=headers)

    return parse_response(
        response
    )  # Make sure you have imported the parse_response function
