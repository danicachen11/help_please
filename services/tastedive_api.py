import requests
import os
from dotenv import load_dotenv

load_dotenv()
TASTE_KEY = os.getenv("TASTEDIVE_KEY")

def get_related_movies(query):
    """
    Takes a song or media query and returns a list of up to 5 related movie names.
    If TasteDive returns nothing, returns a fallback list.
    """
    url = "https://tastedive.com/api/similar"

    params = {
        "q": query,
        "type": "movies",   # get movie recommendations
        "limit": 5,
        "k": TASTE_KEY
    }

    try:
        r = requests.get(url, params=params, timeout=5)
        r.raise_for_status()  # raise error for bad HTTP status
        results = r.json()
    except requests.RequestException as e:
        print(f"TasteDive request failed: {e}")
        # fallback if request fails
        return ["Inception", "La La Land", "The Matrix"]

    # Debug: print API response
    # print("TasteDive response:", results)

    # Check if response has "Similar" and "Results"
    if "Similar" in results and "Results" in results["Similar"]:
        movie_list = [item["Name"] for item in results["Similar"]["Results"]]
        if movie_list:  # non-empty list
            return movie_list

    # Fallback if API returns empty or no results
    return ["Inception", "La La Land", "The Matrix"]

