from flask import Blueprint, redirect, request
from flask import render_template
from models import Post
from flask_paginate import Pagination,get_page_args
import time
import atexit
import importlib
from apscheduler.schedulers.background import BackgroundScheduler

posts = Blueprint('posts',__name__,template_folder='templates')

def get_posts(posts,offset=0, per_page=12):
    return posts[offset: offset + per_page]
@posts.route('/',methods = ['GET'])
def home():
    categories = Post.query.with_entities(Post.category).order_by(Post.id.desc()).group_by(Post.category)
    techs = Post.query.filter_by(category="tech").order_by(Post.id.desc()).all()[:6]
    worlds = Post.query.filter_by(category="world_news").order_by(Post.id.desc()).all()[:6]
    posts = worlds.copy()
    posts.reverse()
    data = worlds+techs
    return render_template('index.html',posts=posts,categories=categories,data=data)



@posts.route('/<category>',methods = ['GET'])
def category(category):
    posts = Post.query.filter_by(category=category).order_by(Post.id.desc()).all()
    page = int(request.args.get('page', 1))
    per_page = 12
    offset = (page - 1) * per_page
    total = len(posts)
    pagination_posts = get_posts(posts,offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')
    posts.reverse()
    return render_template('news.html',data=pagination_posts,page=page,per_page=per_page,pagination=pagination,len=len(pagination_posts),posts=posts)



@posts.route('/<category>/<id>/',methods = ['GET'])
def post(category,id):
    post = Post.query.filter_by(id=id)
    return render_template('post.html',data=post)

@posts.before_app_first_request
def scrape():
    importlib.import_module('data.main')

scheduler = BackgroundScheduler()
scheduler.add_job(func=scrape, trigger="interval", hours=2)
scheduler.start()
