from flask_testing import TestCase
from app import db
from app.test.dummy_data import dummy_data
from manage import app


class BaseTestCase(TestCase):
	""" Base Tests """

	def create_app(self):
		app.config.from_object('app.config.TestingConfig')
		return app

	def setUp(self):
		db.create_all()
		dummy_data()

	def tearDown(self):
		db.session.remove()
		db.drop_all()
