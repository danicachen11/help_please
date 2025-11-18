import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET
))

def get_recent_songs(user_id=None, limit=3):
    """
    Returns a list of recent song dictionaries with name, artist, and features.
    """
    # For simplicity, here we can hardcode popular songs if no user auth:
    songs = [
        {"name": "Shape of You", "artist": "Ed Sheeran", "energy": 0.8, "valence": 0.9},
        {"name": "Blinding Lights", "artist": "The Weeknd", "energy": 0.9, "valence": 0.8},
        {"name": "Rolling in the Deep", "artist": "Adele", "energy": 0.7, "valence": 0.4}
    ]
    return songs
