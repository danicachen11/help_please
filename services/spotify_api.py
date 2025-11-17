import requests
import base64
import os
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

# Get access token
def get_spotify_token():
    auth_string = f"{client_id}:{client_secret}"
    b64 = base64.b64encode(auth_string.encode()).decode()

    url = "https://accounts.spotify.com/api/token"
    headers = {"Authorization": f"Basic {b64}"}
    data = {"grant_type": "client_credentials"}

    r = requests.post(url, headers=headers, data=data)
    return r.json()["access_token"]

def get_song_info(song_name):
    token = get_spotify_token()
    headers = {"Authorization": f"Bearer {token}"}

    search_url = "https://api.spotify.com/v1/search"
    params = {"q": song_name, "type": "track", "limit": 1}

    r = requests.get(search_url, headers=headers, params=params)
    result = r.json()["tracks"]["items"][0]

    song = {
        "name": result["name"],
        "artist": result["artists"][0]["name"],
        "album": result["album"]["name"],
        "cover": result["album"]["images"][0]["url"]
    }

    return song

