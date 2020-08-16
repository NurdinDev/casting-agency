from flask import request, jsonify, abort
from app.model.movie import Movie
from app.model.actor import Actor
from app.auth.auth import AuthError, requires_auth

def init_api(app):

	@app.route('/', methods=['GET'])
	def index():
		"""
		example endpoint
		"""
		return jsonify({
			'success': True
		}), 200

	@app.route('/movies', methods=['GET'])
	def get_movies():
		"""
		Get all movies information
		"""
		movies = Movie.get_all_movies()

		return jsonify({
			'success': True,
			'movies': movies
		})

	@app.route('/movies', methods=['POST'])
	def add_movies():
		"""
		Create new movie record
		"""
		body = request.get_json()
		if not body or 'name' not in body:
			abort(400)

		name = body['name']

		try:
			movie = Movie(name=name)
			movie.save()

			movies = Movie.get_all_movies()

			print(movies)
			return jsonify({
				"success": True,
				"movies": [movie.format() for movie in movies]
			})
		except Exception as e:
			abort(422)

	@app.route('/movie/<int:id>', methods=['PATCH'])
	def patch_movie(id):
		movie = Movie.get_one_movie(id)
		if not movie:
			abort(404)

		try:
			body = request.get_json()
			name = body.get('name', None)
			if name:
				movie.name = name

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

	# Error Handling
	@app.errorhandler(AuthError)
	def handle_auth_error(ex):
		response = jsonify(ex.error)
		response.status_code = ex.status_code
		return response

	@app.errorhandler(422)
	def unprocessable(error):
		return jsonify({
			'success': False,
			'error': 422,
			'message': "unprocessable"
		}), 422

	@app.errorhandler(404)
	def not_found(error):
		return jsonify({
			'success': False,
			'error': 404,
			'message': "resource not found!"
		}), 404

	@app.errorhandler(500)
	def server_error(error):
		return jsonify({
			'success': False,
			'error': 500,
			'message': "internal server error!"
		}), 500

	@app.errorhandler(400)
	def server_error(error):
		return jsonify({
			'success': False,
			'error': 400,
			'message': "Bad Request!"
		}), 400

	@app.errorhandler(AuthError)
	def handle_invalid_usage(error):
		return jsonify({
			"success": False,
			"error": error.status_code,
			"message": error.error
		}), error.status_code
