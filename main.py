
# Initial code to access TMDB API

import requests
import json
from pprint import pprint
from config import api_key

#  Test for one genre

# Pass the Action genre to return the most popular movies from the discover feature
def api_connect():

    genre = "Action"
    page = 1
    query_url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page={page}&"
    response = requests.get(f'{query_url}with_genre={genre}').json()

    # movie_title = response['results'][0]['title']
    # movie_id = response['results'][0]['id']
    # movie_description = response['results'][0]['overview']
    # release_date = response['results'][0]['release_date']
    # avg_score = response['results'][0]['vote_average']
    # backdrop = response['results'][0]['backdrop_path']

    # configuration query
    config_query = f'https://api.themoviedb.org/3/configuration?api_key={api_key}'
    img_response = requests.get(f'{config_query}').json()

    # The 3 components needed to obtain an image
    base_url = img_response['images']['base_url']
    size = img_response['images']['poster_sizes'][6]

    # final query string
    img_query_path = base_url+size


    movie_data = []

    for movie in response['results']:
        movie_title = movie['title']
        movie_id = movie['id']
        movie_description = movie['overview']
        release_date = movie['release_date']
        avg_score = movie['vote_average']
        backdrop = movie['backdrop_path']
        img_url = img_query_path+str(movie['backdrop_path'])

        movie_dict = {
            "Title": movie_title,
            "ID": movie_id,
            "Description": movie_description,
            "Released": release_date,
            "Avg_Score": avg_score,
            "Backdrop Path": backdrop,
            "img_url": img_url
        }

        movie_data.append(movie_dict)


    # movie_data = { 
    #     "title": movie_title,
    #     "id": movie_id,
    #     "description": movie_description,
    #     "release_date": release_date,
    #     "avg_score": avg_score,
    #     "backdrop": backdrop,
    #     "image_url": img_query_path
    # }
    
    return movie_data

# Movie Backdrop

# Explore specific features
