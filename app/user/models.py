from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    surname = db.Column(db.String(255))

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return '<User %d>' % self.id