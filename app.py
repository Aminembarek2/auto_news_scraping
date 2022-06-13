from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask('___name___')
app.config.from_object(Config)

db = SQLAlchemy(app)

