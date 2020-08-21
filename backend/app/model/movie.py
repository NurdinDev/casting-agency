import datetime
from .. import db
from app.model.actor import Actor

actors_movies = db.Table('actors_movies', db.metadata, db.Column('movie_id', db.Integer, db.ForeignKey('movies.id')),
						 db.Column('actor_id', db.Integer, db.ForeignKey('actors.id')))


class Movie(db.Model):
	__tablename__ = 'movies'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(), nullable=False)
	about = db.Column(db.String(), nullable=False)
	actors = db.relationship('Actor', secondary=actors_movies, backref='movies', lazy=True)
	created_at = db.Column(db.DateTime)
	modified_at = db.Column(db.DateTime)

	# class constructor
	def __init__(self, data):
		self.name = data.get('name', None)
		self.about = data.get('about', None)
		actors = data.get('actors', None)
		if actors is not None and isinstance(actors, list):
			for actor in actors:
				if 'id' in actor:
					# get existing one
					self.actors.append(Actor.get_one_actor(actor['id']))
				else:
					actor_exist = Actor.query.filter(Actor.name == actor['name']).first()
					if actor_exist:
						self.actors.append(Actor.get_one_actor(actor_exist.id))
					else:
						# create new one
						self.actors.append(Actor(actor))

		self.created_at = datetime.datetime.utcnow()
		self.modified_at = datetime.datetime.utcnow()

	@staticmethod
	def create_db():
		db.create_all()

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
			'about': self.about,
			'actors': [actor.short_format() for actor in self.actors],
			'created_at': self.created_at,
			'modified_at': self.modified_at
		}

	@staticmethod
	def get_all_movies():
		return Movie.query.all()

	@staticmethod
	def get_one_movie(id):
		return Movie.query.get(id)

	def __repr(self):
		return '<id {}>'.format(self.id)
