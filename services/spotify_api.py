import os
from dotenv import load_dotenv
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

# Load environment variables from .env
load_dotenv()

sp_oauth = SpotifyOAuth(
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),        # matches your .env
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
    scope="user-read-recently-played",
    cache_path=".cache"
)

sp = Spotify(auth_manager=sp_oauth)

def get_recent_songs(limit=3):
    # Mock data for testing
    return [
        {"title": "Shape of You", "artist": "Ed Sheeran"},
        {"title": "Blinding Lights", "artist": "The Weeknd"},
        {"title": "Thriller", "artist": "Michael Jackson"}
    ]



