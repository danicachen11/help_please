import requests
import os
from dotenv import load_dotenv

load_dotenv()
OMDB_KEY = os.getenv("OMDB_KEY")

def get_movie_details(title):
    url = "http://www.omdbapi.com/"
    params = {"t": title, "apikey": OMDB_KEY}

    r = requests.get(url, params=params)
    data = r.json()

    if data.get("Response") == "True":
        return {
            "title": data["Title"],
            "year": data["Year"],
            "plot": data["Plot"],
            "poster": data["Poster"]
        }
    return None

