import datetime
from .. import db


class Actor(db.Model):
	"""
	Actor Model
	"""

	# table name
	__tablename__ = 'actors'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(), nullable=False)
	age = db.Column(db.Integer, nullable=False)
	gender = db.Column(db.String(), nullable=False)
	created_at = db.Column(db.DateTime)
	modified_at = db.Column(db.DateTime)

	# class constructor
	def __init__(self, data):
		"""
		Class constructor
		"""
		self.name = data.get('name')
		self.age = data.get('age')
		self.gender = data.get('gender')
		self.created_at = datetime.datetime.utcnow()
		self.modified_at = datetime.datetime.utcnow()

	def save(self):
		db.session.add(self)
		db.session.commit()

	def update(self, data):
		for key in data:
			setattr(self, key, data.get(key))
		self.modified_at = datetime.datetime.utcnow()
		db.session.commit()

	def delete(self):
		db.session.delete(self)
		db.session.commit()

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'age': self.age,
			'gender': self.gender,
			'created_at': self.created_at,
			'modified_at': self.modified_at
		}

	def short_format(self):
		return {
			'name': self.name
		}

	@staticmethod
	def get_all_actors():
		return Actor.query.all()

	@staticmethod
	def get_one_actor(id):
		return Actor.query.get(id)

	def __repr(self):
		return '<id {}>'.format(self.id)
