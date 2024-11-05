from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Set the Database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)

from app import routes, routes