from flask import request, jsonify, abort
from app.model.movie import Movie

def movie_api(app):
	@app.route('/movies', methods=['GET'])
	def get_movies():
		"""
		Get all movies information
		"""
		movies = Movie.get_all_movies()

		return jsonify({
			'success': True,
			'movies': [movie.format() for movie in movies]
		})

	@app.route('/movies', methods=['POST'])
	def add_movies():
		"""
		Create new movie record
		"""
		body = request.get_json()
		if not body:
			abort(400)

		try:
			movie = Movie(body)
			movie.save()
			movies = Movie.get_all_movies()

			print(movies)
			return jsonify({
				"success": True,
				"movies": [movie.format() for movie in movies]
			})
		except Exception as e:
			print(e)
			abort(422)

	@app.route('/movie/<int:id>', methods=['PATCH'])
	def patch_movie(id):
		movie = Movie.get_one_movie(id)
		if not movie:
			abort(404)

		try:
			body = request.get_json()
			name = body.get('name', None)
			about = body.get('about', None)
			if name:
				movie.name = name
			if about:
				movie.about = about

			movie.update()
			movies = Movie.get_all_movies()

			return jsonify({
				"success": True,
				"movies": [movie.format() for movie in movies]
			})
		except Exception as e:
			abort(422)

	@app.route('/movie/<int:id>', methods=['DELETE'])
	def delete_movie(id):
		movie = Movie.get_one_movie(id)
		if not movie:
			abort(404)
		try:
			movie.delete()
			return jsonify({
				'success': True,
				'delete': id
			})
		except Exception as e:
			abort(422)

