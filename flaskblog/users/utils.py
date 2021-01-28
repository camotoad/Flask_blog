import secrets
import os
from flask_mail import Message
from flask import url_for
from flaskblog import mail, app

def save_picture(picture):
    random = secrets.token_hex(10)
    _, extension = os.path.splitext(picture.filename)
    file_name = random + extension
    picture_path = os.path.join(app.root_path, 'static/pics', file_name)
    picture.save(picture_path)

    return file_name

def send_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', recipients=[user.email])
    msg.body = f'''Please click the link below to reset your password:
{url_for('users.reset_password', token=token, _external=True)}

If you did not make this request, you may ignore this email and no changes will be made.
'''
    mail.send(msg)
