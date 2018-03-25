from flask import request, jsonify, Blueprint, Response
from flask.views import MethodView
from app import app
from app.auth.service import check_auth, create_user

auth_bp = Blueprint('auth_bp', __name__)


class AuthView(MethodView):

    def post(self):
        return jsonify(check_auth(request)), 201


class RegisterView(MethodView):

    def post(self):
        return jsonify(create_user(request)), 201


auth_view = AuthView.as_view('auth_view')
register_view = RegisterView.as_view('register_view')

app.add_url_rule(
    '/auth/login', view_func=auth_view, methods=['POST']
)

app.add_url_rule(
    '/auth/register', view_func=register_view, methods=['POST']
)
