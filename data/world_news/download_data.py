import json
import data.world_news.translatedata
from app import db
from models import Post
with open('data/world_news/data.json','r+') as file:
    file = json.load(file) 
file.reverse()

for i in file:
    post = Post(title=i['title'],description=i['description'],image=i['image'],time=i['time'],category='world_news')
    exists = Post.query.filter_by(title=i['title']).all()
    if not exists:
        db.session.add(post)
        db.session.commit()