from app.model.movie import Movie
from app.model.actor import Actor

movies = [
	{
		'name': 'movie 1',
		'about': 'about movie 1'
	}, {
		'name': 'movie 2',
		'about': 'about movie 2'
	}, {
		'name': 'movie 3',
		'about': 'about movie 3'
	}, {
		'name': 'movie 4',
		'about': 'about movie 4'
	}
]

actors = [
	{
		'name': 'actor 1',
		'age': '29',
		'gender': 'male'
	}, 	{
		'name': 'actor 2',
		'age': '19',
		'gender': 'female'
	}, 	{
		'name': 'actor 3',
		'age': '29',
		'gender': 'male'
	}, 	{
		'name': 'actor 4',
		'age': '29',
		'gender': 'female'
	}
]


def dummy_data():
	for item in range(4):
		actor = Actor(actors[item])
		movie = Movie(movies[item])
		movie.actors.append(actor)
		movie.save()
		actor.save()
