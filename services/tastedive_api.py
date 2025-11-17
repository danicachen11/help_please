import requests
import os
from dotenv import load_dotenv

load_dotenv()
TASTE_KEY = os.getenv("TASTEDIVE_KEY")

def get_related_movies(query):
    url = "https://tastedive.com/api/similar"

    params = {
        "q": query,
        "type": "movies",   
        "limit": 5,
        "k": TASTE_KEY
    }

    r = requests.get(url, params=params)
    results = r.json()

    movie_list = [item["Name"] for item in results["Similar"]["Results"]]
    return movie_list

