from flask import request, jsonify, Blueprint
from app.user.service import UserService as service
from app.auth.service import requires_auth
from flask_restful import Resource, Api


user_bp = Blueprint('user_bp', __name__)
api = Api(user_bp)


class User(Resource):

    @requires_auth
    def get(self, id):
        return jsonify(service.find_one(id))

    @requires_auth
    def put(self, id):
        return jsonify(service.update(request, id)), 200

    @requires_auth
    def delete(self, id):
        service.delete(id)
        return jsonify(dict(result="User deleted")), 204


class Users(Resource):

    @requires_auth
    def get(self):
        return jsonify(service.find_all(1))

    @requires_auth
    def post(self):
        return jsonify(service.create(request))


api.add_resource(User, '/users/<int:id>')
api.add_resource(Users, '/users')
