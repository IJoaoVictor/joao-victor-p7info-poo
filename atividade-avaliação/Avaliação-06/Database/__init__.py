from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os.path

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'Database.db')
app.debug = True

db = SQLAlchemy(app)
