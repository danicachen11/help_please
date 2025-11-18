def feature_to_movie_keyword(song):
    """
    Simple mapping from song features to movie genre keywords.
    """
    energy = song.get("energy", 0.5)
    valence = song.get("valence", 0.5)

    if energy > 0.8 and valence > 0.7:
        return "Action"
    elif valence < 0.4:
        return "Drama"
    elif valence > 0.6:
        return "Comedy"
    else:
        return "Romance"
