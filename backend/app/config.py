import os
from dotenv import load_dotenv

load_dotenv(verbose=False)

postgres_local_base = os.getenv('DATABASE_URL')
postgres_local_base_test = os.getenv('DATABASE_URL_TEST')

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
	DEBUG = False


class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = postgres_local_base
	SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
	DEBUG = True
	TESTING = True
	SQLALCHEMY_DATABASE_URI = postgres_local_base_test
	PRESERVE_CONTEXT_ON_EXCEPTION = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
	DEBUG = False
	SQLALCHEMY_DATABASE_URI = postgres_local_base


config_by_name = dict(
	dev=DevelopmentConfig,
	test=TestingConfig,
	prod=ProductionConfig
)
