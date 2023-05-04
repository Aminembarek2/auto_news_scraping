import os
import urllib.parse 

# Configure your database
params = urllib.parse.quote_plus(os.environ["AWSSQLConnectionString"])

class Config:
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%s'% params
    SQLALCHEMY_TRACK_MODIFICATIONS = False
