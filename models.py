from app import db


class Post(db.Model):
    __tablename__="post"
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    title = db.Column(db.Text,nullable=False, unique=True)
    description = db.Column(db.Text, unique=True, nullable=False)
    image = db.Column(db.Text, unique=True, nullable=False)
    time = db.Column(db.Text, nullable=False)
    category = db.Column(db.Text, nullable=False)
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

    def __repr__(self):
        return '<Post %r>' % self.id
