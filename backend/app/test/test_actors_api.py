from app.test.base import BaseTestCase
import json


class ApiTestCase(BaseTestCase):
	new_actor = {
		'name': "new actor",
		'age': '33',
		'gender': 'male'
	}

	update_actor = {
		'name': "new actor updated"
	}

	new_actor_422 = {
		'name': "new actor"
	}

	def test_index(self):
		res = self.client.get('/')
		data = json.loads(res.data)
		self.assert200(res)
		self.assertEqual(data['success'], True)

	def test_get_actors_unAuthorize(self):
		res = self.client.get('/actors')
		data = json.loads(res.data)
		self.assert401(res)
		self.assertEqual(data['success'], False)

	def test_get_actors(self):
		res = self.client.get('/actors', headers=self.assistant_header)
		data = json.loads(res.data)
		self.assert200(res)
		self.assertEqual(data['success'], True)

	def test_post_actors_assistant_role(self):
		res = self.client.post('/actors', json=self.new_actor, headers=self.assistant_header)
		data = json.loads(res.data)
		self.assert401(res)
		self.assertEqual(data['success'], False)

	def test_post_actors_director_role(self):
		res = self.client.post('/actors', json=self.new_actor, headers=self.director_header)
		data = json.loads(res.data)
		self.assert401(res)
		self.assertEqual(data['success'], False)

	def test_post_actors_producer_role(self):
		res = self.client.post('/actors', json=self.new_actor, headers=self.producer_header)
		data = json.loads(res.data)
		self.assert200(res)
		self.assertEqual(data['success'], True)
		self.assertTrue(len(data['actors']))

	def test_post_actors_unprocessable(self):
		res = self.client.post('/actors', json=self.new_actor_422, headers=self.producer_header)
		data = json.loads(res.data)
		self.assertEqual(res.status_code, 422)
		self.assertEqual(data['success'], False)

	def test_patch_actors_assistant_role(self):
		res = self.client.patch('/actors/1', json=self.update_actor, headers=self.assistant_header)
		data = json.loads(res.data)
		self.assert401(res)
		self.assertEqual(data['success'], False)

	def test_patch_actors_director_role(self):
		res = self.client.patch('/actors/1', json=self.update_actor, headers=self.director_header)
		data = json.loads(res.data)
		self.assert401(res)
		self.assertEqual(data['success'], False)

	def test_patch_actors_producer_role(self):
		res = self.client.patch('/actors/1', json=self.update_actor, headers=self.producer_header)
		data = json.loads(res.data)
		self.assert200(res)
		self.assertEqual(data['success'], True)
		self.assertTrue(len(data['actors']))

	def test_delete_actors_assistant_role(self):
		res = self.client.delete('/actors/1', headers=self.assistant_header)
		data = json.loads(res.data)
		self.assert401(res)
		self.assertEqual(data['success'], False)

	def test_delete_actors_director_role(self):
		res = self.client.delete('/actors/1', headers=self.director_header)
		data = json.loads(res.data)
		self.assert401(res)
		self.assertEqual(data['success'], False)

	def test_delete_actors_producer_role(self):
		res = self.client.delete('/actors/1', headers=self.producer_header)
		data = json.loads(res.data)
		self.assert200(res)
		self.assertEqual(data['success'], True)
		self.assertTrue(data['delete'] == 1)

	def test_delete_actors_producer_role_404(self):
		res = self.client.delete('/actors/11111', headers=self.producer_header)
		data = json.loads(res.data)
		self.assert404(res)
		self.assertEqual(data['success'], False)
