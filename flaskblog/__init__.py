from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SK_FlaskBlog')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fb.db'
db = SQLAlchemy(app)

from flaskblog import routes
