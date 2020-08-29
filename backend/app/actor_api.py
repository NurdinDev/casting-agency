from flask import request, jsonify, abort

from app import requires_auth
from app.model.actor import Actor


def actor_api(app):
	@app.route('/actors', methods=['GET'])
	@requires_auth('get:actors')
	def get_actors(payload):
		"""
		Get all actors information
		"""
		actors = Actor.get_all_actors()

		return jsonify({
			'success': True,
			'actors': [actor.format() for actor in actors]
		})

	@app.route('/actors/<int:actor_id>', methods=['GET'])
	@requires_auth('get:actors')
	def get_single_actor(payload, actor_id):
		"""
		Get single actor information
		"""
		actor = Actor.get_one_actor(actor_id)

		if not actor:
			abort(404)

		return jsonify({
			'success': True,
			'actor': Actor.format(actor)
		})

	@app.route('/actors', methods=['POST'])
	@requires_auth('post:actors')
	def add_actors(payload):
		"""
		Create new actor record
		"""
		body = request.get_json()
		if not body or 'name' not in body:
			abort(400)

		try:
			actor = Actor(body)
			actor.save()

			actors = Actor.get_all_actors()

			return jsonify({
				"success": True,
				"actors": [actor.format() for actor in actors]
			})
		except Exception:
			abort(422)

	@app.route('/actors/<int:actor_id>', methods=['PATCH'])
	@requires_auth('patch:actors')
	def patch_actor(payload, actor_id):
		actor = Actor.get_one_actor(actor_id)
		if not actor:
			abort(404)

		try:
			body = request.get_json()
			actor.update(body)
			actors = Actor.get_all_actors()

			return jsonify({
				"success": True,
				"actors": [actor.format() for actor in actors]
			})
		except Exception:
			abort(422)

	@app.route('/actors/<int:actor_id>', methods=['DELETE'])
	@requires_auth('delete:actors')
	def delete_actor(payload, actor_id):
		actor = Actor.get_one_actor(actor_id)
		if not actor:
			abort(404)
		try:
			actor.delete()
			return jsonify({
				'success': True,
				'delete': actor_id
			})
		except Exception:
			abort(422)
