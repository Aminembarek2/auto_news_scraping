import os

BASE_DIR = os.path.dirname(os.path.abspath(__name__))
URL = os.path.join(BASE_DIR,'posts.db')

class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# postgresql://postgres:root@localhost/posts