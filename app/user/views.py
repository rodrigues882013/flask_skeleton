from flask import request, jsonify, Blueprint, Response
from flask.views import MethodView
from app import db, app
from app.user.service import UserService as service
from app.auth.service import requires_auth

user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/')
@user_bp.route('/home')
def home():
    return "Welcome to the Catalog Home."


class UserView(MethodView):

    @requires_auth
    def get(self, id=None, page=1):
        return jsonify(service.find_all(page) if not id else service.find_one(id))

    @requires_auth
    def post(self):
        return jsonify(service.create(request)), 201

    @requires_auth
    def put(self, id):
        return jsonify(service.update(request, id)), 200

    @requires_auth
    def delete(self, id):
        service.delete(id)
        return jsonify(dict(result="User deleted")), 204


user_view = UserView.as_view('user_view')
app.add_url_rule(
    '/users', view_func=user_view, methods=['GET', 'POST']
)
app.add_url_rule(
    '/users/<int:id>', view_func=user_view, methods=['GET', 'PUT', 'DELETE']
)