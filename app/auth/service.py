import hashlib
import jwt

from functools import wraps
from flask import request, Response, abort
from app.user.service import UserService as service


def check_auth(request):
    auth = request.get_json()

    user = service.find_by_login(auth.get('login'))

    if not user:
        abort(404)
        # return dict(reasom='User not found', code=404)

    if user.get('password') != hashlib.sha224(auth.get('password').encode('utf-8')).hexdigest():
        abort(401)
        # return dict(reasom='Wrong password', code=401)

    token = jwt.encode(user, 'secret', algorithm='HS256')

    return dict(authorized=True, token=str.format('Bearer {0}', token))


def create_user(register_request):
    return service.create(register_request)


def valid_token(token):
    token = token.split(' ')

    if not token[1]:
        return False

    user = jwt.decode(token[1], 'secret', algorithms=['HS256'])

    if not user:
        return False

    return True


def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers['Authorization']
        if not token or not valid_token(token):
            return authenticate()
        return f(*args, **kwargs)
    return decorated