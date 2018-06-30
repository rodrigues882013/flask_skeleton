from flask import Flask

from .extensions import db
from .user import user_bp
from .auth import auth_bp

__all__ = ['create_app', 'app']

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'


def create_app():
    __register_blueprint()
    __configure_extensions()
    __init_db()
    return app


def __register_blueprint():
    app.register_blueprint(user_bp)
    app.register_blueprint(auth_bp)


def __configure_extensions():
    with app.app_context():
        db.init_app(app)


def __init_db():
    with app.app_context():
        db.create_all()
