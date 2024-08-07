from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Book(db.model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return '<Book %r>' % self.title
