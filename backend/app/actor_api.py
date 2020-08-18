from flask import request, jsonify
from app.model.actor import Actor
from werkzeug.exceptions import UnprocessableEntity, HTTPException, abort


def actor_api(app):
	@app.route('/actors', methods=['GET'])
	def get_actors():
		"""
		Get all actors information
		"""
		actors = Actor.get_all_actors()

		return jsonify({
			'success': True,
			'actors': [actor.format() for actor in actors]
		})

	@app.route('/actors/<int:actor_id>', methods=['GET'])
	def get_single_actor(actor_id):
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
	def add_actors():
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
		except HTTPException as e:
			print(e)
			abort(422)

	@app.route('/actors/<int:id>', methods=['PATCH'])
	def patch_actor(id):
		actor = Actor.get_one_actor(id)
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
		except UnprocessableEntity:
			abort(422)

	@app.route('/actors/<int:id>', methods=['DELETE'])
	def delete_actor(id):
		actor = Actor.get_one_actor(id)
		if not actor:
			abort(404)
		try:
			actor.delete()
			return jsonify({
				'success': True,
				'delete': id
			})
		except UnprocessableEntity:
			abort(422)
