from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST', 'localhost')
dbname = os.getenv('DB_NAME')

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}/{dbname}'

db = SQLAlchemy(app)