import os
import urllib.parse 

# Configure your database

class Config:
    
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mysql@localhost/autonews'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
