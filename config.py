import os
# Configure your database
class Config:
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://'+os.environ['MYSQLUSER'] +':'+os.environ['MYSQLPASSWORD']+'@'+os.environ['MYSQLHOST']+':'+os.environ['MYSQLPORT']+'/'+os.environ['MYSQLDATABASE']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
