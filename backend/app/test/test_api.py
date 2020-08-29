import os

from app.test.base import BaseTestCase
import json

director_header = {
	'Authorization': 'Bearer ' + str(os.getenv('DIRECTOR_TOKEN'))
}
assistant_header = {
	'Authorization': 'Bearer ' + str(os.getenv('ASSISTANT_TOKEN'))
}
producer_header = {
	'Authorization': 'Bearer ' + str(os.getenv('PRODUCER_TOKEN'))
}


class ApiTestCase(BaseTestCase):
	new_movie = {
		'name': "new movie",
		'about': "about movie"
	}

	update_movie = {
		'name': "new movie updated"
	}

	new_movie_422 = {
		'name': "new movie"
	}

	def test_index(self):
		res = self.client.get('/')
		data = json.loads(res.data)
		self.assert200(res)
		self.assertEqual(data['success'], True)

	def test_get_movies_unAuthorize(self):
		res = self.client.get('/movies')
		data = json.loads(res.data)
		self.assert401(res)
		self.assertEqual(data['success'], False)

	def test_get_movies(self):
		res = self.client.get('/movies', headers=assistant_header)
		data = json.loads(res.data)
		self.assert200(res)
		self.assertEqual(data['success'], True)

	def test_post_movie_assistant_role(self):
		res = self.client.post('/movies', json=self.new_movie, headers=assistant_header)
		data = json.loads(res.data)
		self.assert401(res)
		self.assertEqual(data['success'], False)

	def test_post_movie_director_role(self):
		res = self.client.post('/movies', json=self.new_movie, headers=director_header)
		data = json.loads(res.data)
		self.assert401(res)
		self.assertEqual(data['success'], False)

	def test_post_movie_producer_role(self):
		res = self.client.post('/movies', json=self.new_movie, headers=producer_header)
		data = json.loads(res.data)
		self.assert200(res)
		self.assertEqual(data['success'], True)
		self.assertTrue(len(data['movies']))

	def test_post_movie_unprocessable(self):
		res = self.client.post('/movies', json=self.new_movie_422, headers=producer_header)
		data = json.loads(res.data)
		self.assertEqual(res.status_code, 422)
		self.assertEqual(data['success'], False)

	def test_patch_movie_assistant_role(self):
		res = self.client.patch('/movies/1', json=self.update_movie, headers=assistant_header)
		data = json.loads(res.data)
		self.assert401(res)
		self.assertEqual(data['success'], False)

	def test_patch_movie_director_role(self):
		res = self.client.patch('/movies/1', json=self.update_movie, headers=director_header)
		data = json.loads(res.data)
		self.assert401(res)
		self.assertEqual(data['success'], False)

	def test_patch_movie_producer_role(self):
		res = self.client.patch('/movies/1', json=self.update_movie, headers=producer_header)
		data = json.loads(res.data)
		self.assert200(res)
		self.assertEqual(data['success'], True)
		self.assertTrue(len(data['movies']))

	def test_delete_movie_assistant_role(self):
		res = self.client.delete('/movies/1', headers=assistant_header)
		data = json.loads(res.data)
		self.assert401(res)
		self.assertEqual(data['success'], False)

	def test_delete_movie_director_role(self):
		res = self.client.delete('/movies/1', headers=director_header)
		data = json.loads(res.data)
		self.assert401(res)
		self.assertEqual(data['success'], False)

	def test_delete_movie_producer_role(self):
		res = self.client.delete('/movies/1', headers=producer_header)
		data = json.loads(res.data)
		self.assert200(res)
		self.assertEqual(data['success'], True)
		self.assertTrue(len(data['movies']))
