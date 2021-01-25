from flask import Flask
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SK_FlaskBlog')

from flaskblog import routes
