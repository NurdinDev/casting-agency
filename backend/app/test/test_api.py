from app.test.base import BaseTestCase
import json


class ApiTestCase(BaseTestCase):
	new_movie = {
		'name': "new movie",
		'about': "about movie"
	}

	new_movie_422 = {
		'name': "new movie"
	}

	def test_index(self):
		res = self.client.get('/')
		data = json.loads(res.data)
		self.assert200(res)
		self.assertEqual(data['success'], True)

	def test_get_movies(self):
		res = self.client.get('/movies')
		data = json.loads(res.data)
		self.assert200(res)
		self.assertEqual(data['success'], True)

	def test_post_movie(self):
		res = self.client.post('/movies', json=self.new_movie)
		data = json.loads(res.data)
		self.assert200(res)
		self.assertEqual(data['success'], True)
		self.assertTrue(len(data['movies']))

	def test_post_movie_422(self):
		res = self.client.post('/movies', json=self.new_movie_422)
		data = json.loads(res.data)
		self.assertEqual(res.status_code, 422)
		self.assertEqual(data['success'], False)
