from app.model.movie import Movie

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


def init_movie_dummy_data():
	for movie in movies:
		mov = Movie(movie)
		mov.save()
