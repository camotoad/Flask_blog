from flaskblog import db
from flaskblog.models import User, Post

db.create_all()
new = User(username='admin', email='admin@flaskblog.com', password='asdf')
new2 = User(username='test', email='test@test.com', password='asdf')
db.session.add(new)
db.session.add(new2)
post1 = Post(title='Post 1', content='This is the first post, by admin', user_id=1)
db.session.add(post1)
post2 = Post(title='Post 2', content='This is the second post, by admin', user_id=1)
db.session.add(post2)
post3 = Post(title='Post 3', content='This is the first post, by test', user_id=2)
db.session.add(post3)
db.session.commit()