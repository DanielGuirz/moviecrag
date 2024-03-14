# import api
from movie_api import MovieAPI

# initialize api
api = MovieAPI()

# search for entity
movies = api.get_movie_info("the avenGers")
print("Title for first result", movies[0]['title'])

# get an actor from entity
actor = movies[0]['cast'][0]['id']

# directly lookup this person by id
person_info = api.get_person_info_by_id(actor)

# get his name and birth date
print("First actor name: ", person_info['name'])
print("First actor birth date: ", person_info['birthday'])
