from flask import Flask, render_template, request
from services.spotify_api import get_recent_songs
from services.tastedive_api import get_similar_movies
from services.omdb_api import get_movie_details

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = []

    if request.method == "POST":
        # Get 3 recent songs from Spotify
        songs = get_recent_songs()

        for song in songs:
            title = song["title"]
            artist = song["artist"]

            # TasteDive → get similar movies
            movies = get_similar_movies(f"{title} {artist}")

            movie_details = []
            for movie in movies:
                details = get_movie_details(movie)
                if details:
                    movie_details.append(details)

            recommendations.append({
                "song": title,
                "artist": artist,
                "movies": movie_details
            })

    return render_template("index.html", recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)
