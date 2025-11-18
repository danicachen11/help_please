import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp_oauth = SpotifyOAuth(
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
    redirect_uri="http://localhost/",  # dummy, not actually used
    scope="user-read-recently-played",
    show_dialog=True
)

# Step 1: get auth URL
auth_url = sp_oauth.get_authorize_url()
print("Go here and authorize:", auth_url)

# Step 2: paste the URL Spotify redirects you to
response = input("Paste the full URL you were redirected to: ")

# Step 3: parse code and get token
code = sp_oauth.parse_response_code(response)
token_info = sp_oauth.get_access_token(code)

# Step 4: create Spotify client
sp = spotipy.Spotify(auth=token_info['access_token'])

# Example: get last 3 songs
results = sp.current_user_recently_played(limit=3)
for item in results['items']:
    track = item['track']
    print(track['name'], "by", track['artists'][0]['name'])
