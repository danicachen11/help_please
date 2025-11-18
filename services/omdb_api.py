import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_movie_details(title):
    url = "http://www.omdbapi.com/"
    params = {
        "t": title,
        "apikey": os.getenv("OMDB_API_KEY")
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data.get("Response") == "True":
        return {
            "title": data.get("Title"),
            "year": data.get("Year"),
            "plot": data.get("Plot"),
            "poster": data.get("Poster")
        }
    return None
