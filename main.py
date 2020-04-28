
# Initial code to access TMDB API

import requests
import json
from pprint import pprint
from config import api_key

#  Test for one genre

# Pass the Action genre to return the most popular movies from the discover feature
genre = "Action"
page = 1
query_url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page={page}&"
response = requests.get(f'{query_url}with_genre={genre}').json()
pprint(response)

# Traverse the API

# Explore specific features
