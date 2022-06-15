import json
import data.tech.translatedata
from app import db
from models import Post
with open('data/tech/data.json','r+') as file:
    file = json.load(file) 
file.reverse()

db.create_all()
for i in file:
    post = Post(title=i['title'],description=i['description'],image=i['image'],time=i['time'],category='tech')
    exists = Post.query.filter_by(title=i['title']).all()
    if not exists:
        db.session.add(post)
        db.session.commit()
db.session.close()