import email
from enum import unique
from operator import index
from . import db, login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(100))
    bio = db.Column(db.String(255))
    email = db.Column(db.String(100),nullable = False,unique = True)
    avatar = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    password_secure = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    blog = db.relationship('Blog', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')
    
    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)


    def __repr__(self):
        return f'User {self.username}'

class Blogs(db.Model):

    __tablename__ = 'Blog'
    id = db.Column(db.Integer,primary_key=True)
    company = db.Column(db.String)
    context = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    upvote = db.relationship('Upvote',backref='post',lazy='dynamic')
    downvote = db.relationship('Downvote',backref='post',lazy='dynamic')
    comment = db.relationship('Comment',backref='post',lazy='dynamic')
    delete = db.relationship('Delete',backref = 'post',lazy='dynamic')
 
    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    def _repr_(self):
        return f'Blog{self.company}'

class Subscriber(db.Model):
    __tablename__ = 'subscriber'
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(255), unique=True, index=True)

    def save_subscribers(self):
        db.session.add(self)
        db.session.commit()
    

    def __repr__(self):
        return f'User {self.email}'

class Upvote(db.Model):

    _tablename_ = 'upvotes'

    id = db.Column(db.Integer, primary_key=True)
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_upvotes(cls, id):
        upvote = Upvote.query.filter_by(blog_id=id).all()
        return upvote

    def _repr_(self):
        return f'{self.blog_id}'

class Delete(db.Model):

    __tablename__ = 'delete'
    id = db.Column(db.Integer,primary_key = True)
    blog_id = db.Column(db.Integer,db.ForeignKey('blog.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_deletes(cls,id):
        delete = Delete.query.filter_by(blog_id=id).all()
        return delete

    def _repr_(self):
        return f'{self.blog_id}'

class Comment(db.Model):
    
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.Text(),nullable = False)
    blog_id = db.Column(db.Integer,db.ForeignKey('blog.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,blog_id):
        comments = Comment.query.filter_by(blog_id = blog_id).all()

        return comments

    def __repr__(self):
        return f'comment:{self.comment}'

        
class Downvote(db.Model):

    _tablename_ = 'downvotes'

    id = db.Column(db.Integer, primary_key=True)
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_downvotes(cls, id):
        downvote = Downvote.query.filter_by(blog_id=id).all()
        return downvote

    def _repr_(self):
        return f'{self.blog_id}'

class Quote:
    '''
    Class that returns quotes requested from the quote API
    '''
    def __init__(self, author, quote):
        self.author = author
        self.quote = quote


