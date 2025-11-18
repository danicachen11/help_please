import requests
import os
from dotenv import load_dotenv

load_dotenv()
OMDB_KEY = os.getenv("OMDB_API_KEY")

def search_movies_by_keyword(keyword, limit=5):
    """
    Searches OMDb for movies matching a keyword.
    Returns list of dicts: title, year, plot, poster
    """
    movies = []
    for i in range(1, limit+1):
        url = f"http://www.omdbapi.com/?apikey={OMDB_KEY}&s={keyword}&type=movie&page={i}"
        r = requests.get(url)
        data = r.json()
        if data.get("Search"):
            for movie in data["Search"]:
                movies.append({
                    "title": movie["Title"],
                    "year": movie.get("Year", ""),
                    "imdb_id": movie.get("imdbID", "")
                })
        else:
            break
    # Add plot and poster for first few movies
    for m in movies[:limit]:
        r = requests.get(f"http://www.omdbapi.com/?apikey={OMDB_KEY}&i={m['imdb_id']}")
        info = r.json()
        m["plot"] = info.get("Plot", "No plot available")
        m["poster"] = info.get("Poster", "")
    return movies[:limit]

