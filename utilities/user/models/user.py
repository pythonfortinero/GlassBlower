from manage import app, db 
from sqlalchemy import ForeignKey
from passlib.apps import custom_app_context as pwd_context
from sqlalchemy.orm import relationship 
import datetime

class User(db.Model): 

    __tablename__ = "user" 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column('username', db.String(32))
    password = db.Column('password' , db.String(64))
    email = db.Column('email',db.String(50),unique=True , index=True)
    registered_on = db.Column('registered_on' , db.DateTime)
 
    def __init__(self , username ,password , email):
        self.username = username
        self.hash_password(password)
        self.email = email
        self.registered_on = datetime.datetime.utcnow()

    def get_name(self):
        return self.username

    def hash_password(self, password):
        self.password = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<name {}'.format(self.username)