import os
import requests
from dotenv import load_dotenv
import time

load_dotenv()

class SpotifyAuth:
    def __init__(self):
        load_dotenv()
        self.client_id = os.getenv('CLIENT_ID')
        self.client_secret = os.getenv('CLIENT_SECRET')
        self.redirect_uri = 'http://localhost:8000/home/callback/'

    def get_auth_url(self):
        scope = "streaming user-modify-playback-state user-read-playback-state"
        state = self.generate_random_string(16)
        auth_query_parameters = {
            'response_type': 'code',
            'client_id': self.client_id,
            'scope': scope,
            'redirect_uri': self.redirect_uri,
            'state': state
        }
        return f"https://accounts.spotify.com/authorize/?{requests.compat.urlencode(auth_query_parameters)}"

    def exchange_token(self, code):
        response = requests.post('https://accounts.spotify.com/api/token', {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': self.redirect_uri,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
        })
        if response.status_code != 200:
            raise Exception(f"Error exchanging token: {response.text}")
        return response.json()

    @staticmethod
    def generate_random_string(length):
        import random
        import string
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    def get_token(self, reuests):
        access_token = request.session.get('access_token')
        refresh_token = request.session.get('refresh_token')
        expires_at = request.session.get('expires_at', 3600)

        if time.time() > expires_at:
            token_info = self.refresh_access_token(refresh_token)
            access_token = token_info['access_token']
            request.session['access_token'] = access_token
            request.session['expires_at'] = time.time() + token_info['expires_in']

        return access_token

    def refresh_access_token(self, refresh_token):
        response = requests.post('https://accounts.spotify.com/api/token', {
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
        })
        if response.status_code != 200:
            raise Exception(f"Error refreshing token: {response.text}")
        return response.json()


class MockRequest:
    def __init__(self):
        self.session = {
            'access_token': f'{os.getenv('CLIENT_ID')}',  # Replace with a valid token for testing
            'refresh_token': f'{os.getenv('CLIENT_SECRET')}',  # Replace with a valid refresh token
            'expires_at': time.time() + 3600  # Assume not expired
        }
'''
# Create an instance of SpotifyAuth
autho = SpotifyAuth()

# Create a mock request
mock_request = MockRequest()

# Call the get_token method with the mock request
print(autho.get_token(mock_request))
'''