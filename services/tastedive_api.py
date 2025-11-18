import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_similar_movies(query):
    url = "https://tastedive.com/api/similar"
    params = {
        "q": query,
        "type": "movies",
        "k": os.getenv("TASTEDIVE_API_KEY")
    }

    response = requests.get(url, params=params)
    data = response.json()

    try:
        results = data["Similar"]["Results"]
        return [item["Name"] for item in results][:3]
    except:
        return []
