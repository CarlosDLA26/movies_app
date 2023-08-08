# External libraries
import json


with open('./db/movies.json') as file:
    data_movies = json.load(file)

print('se obtuvo de nuevo')
