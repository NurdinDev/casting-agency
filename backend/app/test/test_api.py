import unittest
from app.test.base import BaseTestCase
import json

class ApiTestCase(BaseTestCase):
  def test_get_movies(self):
    res = self.client.get('/')
    data = json.loads(res.data)
    self.assertEqual(res.status_code, 200)
