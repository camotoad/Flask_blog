from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SK_FlaskBlog')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fb.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'danger'

app.config['MAIL_SERVER'] = 'smtp.mail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('FLASK_EMAIL')
app.config['MAIL_USERNAME'] = os.environ.get('FLASK_EMAIL')
app.config['MAIL_PASSWORD'] = os.environ.get('FLASK_PASS')
mail = Mail(app)

from flaskblog.main.routes import main
from flaskblog.users.routes import users
from flaskblog.posts.routes import posts

app.register_blueprint(main)
app.register_blueprint(users)
app.register_blueprint(posts)
