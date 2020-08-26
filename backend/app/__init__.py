from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from .config import config_by_name
from app.auth.auth import AuthError, requires_auth, AUTH0_DOMAIN, API_AUDIENCE
from werkzeug.exceptions import HTTPException, UnprocessableEntity, Forbidden, NotFound, InternalServerError, BadRequest
import json

db = SQLAlchemy()


def create_app(config_name):
	app = Flask(__name__)
	CORS(app, resources={r"*": {"origins": "*"}})
	app.config.from_object(config_by_name[config_name])
	db.init_app(app)

	from app.movie_api import movie_api
	from app.actor_api import actor_api

	@app.route('/', methods=['GET'])
	def index():
		"""
		example endpoint
		"""
		return jsonify({
			'success': True
		}), 200

	movie_api(app)
	actor_api(app)

	# Error Handling
	@app.errorhandler(AuthError)
	def handle_auth_error(ex):
		response = jsonify(ex.error)
		response.status_code = ex.status_code
		return response

	@app.errorhandler(UnprocessableEntity)
	def unprocessable(self):
		return jsonify({
			'success': False,
			'error': 422,
			'message': "The information you provided incorrect."
		}), 422

	@app.errorhandler(Forbidden)
	def forbidden():
		return jsonify({
			'success': False,
			'error': 403,
			'message': "You don't have the permission for request the resource."
		}), 403

	@app.errorhandler(NotFound)
	def not_found(self):
		return jsonify({
			'success': False,
			'error': 404,
			'message': "Resource not found!"
		}), 404

	@app.errorhandler(InternalServerError)
	def server_error(self):
		return jsonify({
			'success': False,
			'error': 500,
			'message': "Internal server error!"
		}), 500

	@app.errorhandler(BadRequest)
	def bad_request(self):
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

	@app.errorhandler(HTTPException)
	def handle_exception(e):
		response = e.get_response()
		response.data = json.dumps({
			"code": e.code,
			"name": e.name,
			"description": e.description,
		})
		response.content_type = "application/json"
		return response

	return app
