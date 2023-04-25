from django.conf import settings
from django.shortcuts import render

from .interfaces import exchange_code


def github_login(request):
    context = {"client_id": settings.GITHUB_CLIENT_ID}
    return render(request, "github_login.html", context)


def callback(request):
    if code := request.GET.get("code", None):
        token_data = exchange_code(code)

        if "access_token" in token_data:
            token = token_data["access_token"]

            context = {
                "message": f"Successfully authorized! Got code {code} and exchanged it for a user access token ending in {token[-9:]}."
            }
        else:
            context = {
                "message": f"Authorized, but unable to exchange code {code} for token."
            }
    else:
        context = {"message": "Authorization code not provided."}

    return render(request, "callback.html", context)
