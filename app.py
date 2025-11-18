from flask import Flask, render_template
from services.spotify_api import get_recent_songs
from services.song_to_movie import feature_to_movie_keyword
from services.omdb_api import search_movies_by_keyword

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/recommend")
def recommend():
    songs = get_recent_songs()  # last 3 songs
    recommendations = []

    for song in songs:
        keyword = feature_to_movie_keyword(song)
        movies = search_movies_by_keyword(keyword)
        recommendations.append({
            "song": song["name"],
            "artist": song["artist"],
            "movies": movies
        })

    return render_template("results.html", recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)
