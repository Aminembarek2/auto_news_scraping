import os
import urllib.parse 

# Configure your database
params = urllib.parse.quote_plus(os.environ["AzureSQLConnectionString"])

class Config:
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc:///?odbc_connect=%s'% params
    SQLALCHEMY_TRACK_MODIFICATIONS = False
