from app import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(64))


    def __repr__(self):
        return f'<User {self.username}>'


books_authors = db.Table('books_authors',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True),
    db.Column('author_id', db.Integer, db.ForeignKey('author.id'), primary_key=True)
)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    authors = db.relationship('Author', secondary=books_authors, lazy='subquery',
        backref=db.backref('books', lazy=True))

    def __repr__(self):
        return f'<Book {self.title}>'


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(250), unique=True, nullable=False)

    def __repr__(self):
        return f'{self.first_name}'

# db.create_all()