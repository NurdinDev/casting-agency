from app.test.base import BaseTestCase
import json


class ApiTestCase(BaseTestCase):

	def setUp(self):
		self.new_movie = {
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
		# self.assertTrue(len(data['movies']))
