import datetime
from .. import db


class Movie(db.Model):
	__tablename__ = 'movies'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(), nullable=False)
	created_at = db.Column(db.DateTime)
	modified_at = db.Column(db.DateTime)

	# class constructor
	def __init__(self, name):
		self.name = name
		self.created_at = datetime.datetime.utcnow()
		self.modified_at = datetime.datetime.utcnow()

	def save(self):
		db.session.add(self)
		db.session.commit()

	def update(self, data):
		for key, item in data.items():
			setattr(self, key, item)
		self.modified_at = datetime.datetime.utcnow()
		db.session.commit()

	def delete(self):
		db.session.delete(self)
		db.session.commit()

	def format(self):
		return {
			'id': self.id,
			'name': self.name
		}

	@staticmethod
	def get_all_movies():
		return Movie.query.all()

	@staticmethod
	def get_one_movie(id):
		return Movie.query.get(id)

	def __repr(self):
		return '<id {}>'.format(self.id)
