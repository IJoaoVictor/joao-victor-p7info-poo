import os.path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'Database.db') #'sqlite:///C:\\Users\\SAMSUNG\\Desktop\\Avaliação-06\\Database\\Database.db'
app.debug = True

db = SQLAlchemy(app)