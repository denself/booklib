__author__ = 'denself'


import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'base.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
static_dir = "/static"


CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'