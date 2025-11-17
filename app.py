from flask import Flask, render_template, request
from services.spotify_api import get_song_info
from services.tastedive_api import get_related_movies
from services.omdb_api import get_movie_details

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    song_name = request.form["song"]

    # Step 1: get song info
    song_info = get_song_info(song_name)

    # Step 2: get related movies
    movie_names = get_related_movies(song_name)

    # Step 3: get OMDb details for each movie
    movie_details = []
    for title in movie_names:
        details = get_movie_details(title)
        if details:
            movie_details.append(details)

    return render_template(
        "results.html", 
        song=song_info, 
        movies=movie_details
    )

if __name__ == "__main__":
    app.run(debug=True)

