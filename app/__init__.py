from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/app.db'
db = SQLAlchemy(app)

from app.user.views import user_bp
from app.auth.views import auth_bp

app.register_blueprint(user_bp)
app.register_blueprint(auth_bp)

db.create_all()
