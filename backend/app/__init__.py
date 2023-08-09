from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

app = Flask(__name__)
app.config.from_pyfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../config.py'))

db = SQLAlchemy(app)
login_manager = LoginManager(app)
