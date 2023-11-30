import os
basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'secret'

SQLALCHEMY_DATABASE_URI = 'sqlite:///E:/python/python-main/lab8/instance/db.sqlite'
SQLALCHEMY_TRACK_MODIFICATIONS = False