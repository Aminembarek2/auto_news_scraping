import sqlite3
import json
import data.tech.translatedata

conn = sqlite3.connect('posts.db')
cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS post(id INTEGER PRIMARY KEY AUTOINCREMENT, title varchar unique,description varchar,image varchar,time varchar,category varchar);')

with open('data/tech/data.json','r+') as file:
    file = json.load(file) 
file.reverse()
for i in file:
    cur.execute("SELECT title FROM post where title = ?;",(i['title'],))
    exists = cur.fetchone()
    if not exists:
        cur.execute('INSERT INTO post (title,description,image,time,category) VALUES (?,?,?,?,"tech");',(i['title'],i['description'],i['image'],i['time']))
    conn.commit()
cur.close()
conn.close()