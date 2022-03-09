from email.policy import default
from unicodedata import category
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from sqlalchemy.sql import func

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    pitches = db.relationship('Pitch', backref = 'user', lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key = True)
    category = db.Column(db.String(50))
    date_created = db.Column(db.DateTime(timezone = True), default = func.now())
    content = db.Column(db.String())
    upvotes = db.Column(db.Integer, default = 0)
    downvotes = db.Column(db.Integer, default = 0)
    author = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'{self.category}'