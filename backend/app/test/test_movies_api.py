from app.test.base import BaseTestCase
import json


class ApiTestCase(BaseTestCase):
	new_movie = {
		'name': "new movie",
		'about': "about movie"
	}

	update_movie = {
		'name': "new movie updated"
	}

	new_movies_422 = {
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
		res = self.client.get('/movies', headers=self.assistant_header)
		data = json.loads(res.data)
		self.assert200(res)
		self.assertEqual(data['success'], True)

	def test_post_movies_assistant_role(self):
		res = self.client.post('/movies', json=self.new_movie, headers=self.assistant_header)
		data = json.loads(res.data)
		self.assert401(res)
		self.assertEqual(data['success'], False)

	def test_post_movies_director_role(self):
		res = self.client.post('/movies', json=self.new_movie, headers=self.director_header)
		data = json.loads(res.data)
		self.assert401(res)
		self.assertEqual(data['success'], False)

	def test_post_movies_producer_role(self):
		res = self.client.post('/movies', json=self.new_movie, headers=self.producer_header)
		data = json.loads(res.data)
		self.assert200(res)
		self.assertEqual(data['success'], True)
		self.assertTrue(len(data['movies']))

	def test_post_movies_unprocessable(self):
		res = self.client.post('/movies', json=self.new_movies_422, headers=self.producer_header)
		data = json.loads(res.data)
		self.assertEqual(res.status_code, 422)
		self.assertEqual(data['success'], False)

	def test_patch_movies_assistant_role(self):
		res = self.client.patch('/movies/1', json=self.update_movie, headers=self.assistant_header)
		data = json.loads(res.data)
		self.assert401(res)
		self.assertEqual(data['success'], False)

	def test_patch_movies_director_role(self):
		res = self.client.patch('/movies/1', json=self.update_movie, headers=self.director_header)
		data = json.loads(res.data)
		self.assert200(res)
		self.assertEqual(data['success'], True)

	def test_patch_movies_producer_role(self):
		res = self.client.patch('/movies/1', json=self.update_movie, headers=self.producer_header)
		data = json.loads(res.data)
		self.assert200(res)
		self.assertEqual(data['success'], True)
		self.assertTrue(len(data['movies']))

	def test_delete_movies_assistant_role(self):
		res = self.client.delete('/movies/1', headers=self.assistant_header)
		data = json.loads(res.data)
		self.assert401(res)
		self.assertEqual(data['success'], False)

	def test_delete_movies_director_role(self):
		res = self.client.delete('/movies/1', headers=self.director_header)
		data = json.loads(res.data)
		self.assert401(res)
		self.assertEqual(data['success'], False)

	def test_delete_movies_producer_role(self):
		res = self.client.delete('/movies/1', headers=self.producer_header)
		data = json.loads(res.data)
		self.assert200(res)
		self.assertEqual(data['success'], True)
		self.assertTrue(data['delete'] == 1)

	def test_delete_movies_producer_role_404(self):
		res = self.client.delete('/movies/11111', headers=self.producer_header)
		data = json.loads(res.data)
		self.assert404(res)
		self.assertEqual(data['success'], False)
