import os
import random
import string
from django.shortcuts import redirect
from django.http import JsonResponse
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

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
    sp_oauth = SpotifyOAuth(client_id, client_secret, redirect_uri, scope=scope)
    token_info = sp_oauth.get_access_token(request.GET.get('code'))
    
    if token_info:
        access_token = token_info['access_token']
        print('Este es el access token:', access_token)
        # Aquí puedes guardar el token o usarlo según sea necesario
        return redirect('http://127.0.0.1:8000/home/')  # Redirige a la página deseada
    else:
        return JsonResponse({'error': 'Failed to obtain access token'}, status=400)
