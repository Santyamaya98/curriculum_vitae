import os
import random
import string
import requests
from django.shortcuts import redirect
from django.http import JsonResponse

from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import base64
# Cargar variables de entorno
load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
redirect_uri = os.getenv('REDIRECT_URI')


# Configurar el alcance
scope = "streaming user-read-email user-read-private"

def generate_random_string(length):
    possible = string.ascii_letters + string.digits  # A-Z, a-z, 0-9
    return ''.join(random.choice(possible) for _ in range(length))

def login(request):
    sp_oauth = SpotifyOAuth(client_id, client_secret, redirect_uri, scope=scope)
    return redirect(sp_oauth.get_authorize_url())

def callback(request):
    code = request.GET.get('code')
    print(f"Authorization code: {code}")
    if not code:
        return JsonResponse({'error': 'Authorization code not provided'}, status=400)

    auth_string = f"{client_id}:{client_secret}"
    auth_bytes = auth_string.encode("utf-8") 
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = { 
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": redirect_uri  # Ensure this matches the registered URI
    }
    
    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        json_result = response.json()
        access_token = json_result.get("access_token")
        refresh_token = json_result.get("refresh_token")  # You may want to store this for future use

        # save access and refresh token 
        request.session["access_token"] = access_token
        request.session["refresh_token"] = refresh_token

        return redirect('Home')
    else:
        return JsonResponse({'error': 'Failed to obtain access token'}, status=response.status_code)
    
def get_access_token(request):
    # Verificar si el token está en la sesión
    access_token = request.session.get('access_token')
    if not access_token:
        return JsonResponse({'error': 'Access token not found'}, status=404)
    
    return JsonResponse({'access_token': access_token})

#def get_auth_header(token):
#   return {"Authorization": "Bearer " + token}
