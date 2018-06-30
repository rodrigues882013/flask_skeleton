from flask import request, jsonify, Blueprint
from .service import check_auth, create_user

auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth')


@auth_bp.route('/login', methods=['POST'])
def login():
    return jsonify(check_auth(request)), 201


@auth_bp.route('/register', methods=['POST'])
def register():
    return jsonify(create_user(request)), 201
