from flask import request, jsonify, abort
from flask_cors import cross_origin

from app import requires_auth
from app.model.movie import Movie


def movie_api(app):
	@app.route('/movies', methods=['GET'])
	@cross_origin(headers=["Content-Type", "Authorization"])
	@requires_auth('get:movies')
	def get_movies(payload):
		"""
		Get all movies information
		"""
		movies = Movie.get_all_movies()

		return jsonify({
			'success': True,
			'movies': [movie.format() for movie in movies]
		})

	@app.route('/movies/<int:movie_id>', methods=['GET'])
	@cross_origin(headers=["Content-Type", "Authorization"])
	@requires_auth('get:movies')
	def get_single_movie(payload, movie_id):
		"""
		Get single movies information
		"""
		movie = Movie.get_one_movie(movie_id)

		if not movie:
			abort(404)

		return jsonify({
			'success': True,
			'movie': Movie.format(movie)
		})

	@app.route('/movies', methods=['POST'])
	@cross_origin(headers=["Content-Type", "Authorization"])
	@requires_auth('post:movies')
	def add_movies(payload):
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

			return jsonify({
				"success": True,
				"movies": [movie.format() for movie in movies]
			})
		except Exception:
			abort(422)

	@app.route('/movies/<int:movie_id>', methods=['PATCH'])
	@cross_origin(headers=["Content-Type", "Authorization"])
	@requires_auth('patch:movies')
	def patch_movie(payload, movie_id):
		movie = Movie.get_one_movie(movie_id)
		if not movie:
			abort(404)

		try:
			body = request.get_json()
			movie.update(body)
			movies = Movie.get_all_movies()

			return jsonify({
				"success": True,
				"movies": [movie.format() for movie in movies]
			})
		except Exception:
			abort(422)

	@app.route('/movies/<int:movie_id>', methods=['DELETE'])
	@cross_origin(headers=["Content-Type", "Authorization"])
	@requires_auth('delete:movies')
	def delete_movie(payload, movie_id):
		movie = Movie.get_one_movie(movie_id)
		if not movie:
			abort(404)
		try:
			movie.delete()
			return jsonify({
				'success': True,
				'delete': movie_id
			})
		except Exception:
			abort(422)
