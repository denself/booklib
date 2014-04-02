# -*- coding: utf-8 -*-#

from app import db


ROLE_USER = 0
ROLE_ADMIN = 1


class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'sqlite_autoincrement': True}
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(64))
    role = db.Column(db.Integer, default=ROLE_USER)

    def __init__(self, username=None, email=None, password='1111', role=0):
        self.username = username
        self.email = email
        self.password = password
        self.role = role

    def __repr__(self):
        return '<User %r>' % self.username

    def is_active(self):
        return True
    def is_authenticated(self):
        return True
    def is_anonymous(self):
        return False
    def is_admin(self):
        return self.role
    def get_id(self):
        return self.id


association_table = db.Table('association', db.metadata,
                             db.Column('book_id', db.Integer, db.ForeignKey('book.id')),
                             db.Column('author_id', db.Integer, db.ForeignKey('author.id')))


class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, nullable=False)
    authors = db.relationship("Author",
                              secondary=association_table,
                              backref="books")


class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, nullable=False)