from flask_backbone.app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    login = db.Column(db.String(30))
    password = db.Column(db.String(30))

    def __init__(self, first_name, last_name, email, login, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.login = login
        self.password = password

    def __repr__(self):
        return '<User %d>' % self.id