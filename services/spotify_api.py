import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

def get_recent_songs():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
    redirect_uri="http://127.0.0.1:9999/callback",
    scope="user-read-recently-played"
))



    results = sp.current_user_recently_played(limit=3)

    songs = []
    for item in results["items"]:
        track = item["track"]
        songs.append({
            "title": track["name"],
            "artist": track["artists"][0]["name"]
        })

    return songs
