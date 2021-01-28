import os

class Config:
    SECRET_KEY = os.environ.get('SK_FlaskBlog')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///fb.db'
    MAIL_SERVER = 'smtp.mail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_DEFAULT_SENDER = os.environ.get('FLASK_EMAIL')
    MAIL_USERNAME = os.environ.get('FLASK_EMAIL')
    MAIL_PASSWORD = os.environ.get('FLASK_PASS')