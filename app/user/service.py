from app import db
from app.user.models import User
from flask import abort


class UserService:

    @staticmethod
    def create(request):
        user_dto = request.get_json()
        name = user_dto.get('name')
        surname = user_dto.get('surname')

        if not name or not surname:
            abort(400)

        user = User(name, surname)
        db.session.add(user)
        db.session.commit()

        return dict(id=user.id,
                    name=user.name,
                    surname=user.surname)

    @staticmethod
    def find_all(page=1):
        return [dict(id=u.id,
                     name=u.name,
                     surname=u.surname) for u in User.query.paginate(page, 10).items]

    @staticmethod
    def update(request, id):

        user_dto = request.get_json()
        name = user_dto.get('name')
        surname = user_dto.get('surname')
        user = User.query.filter_by(id=id).first()

        if not user:
            abort(404)

        if not name or not surname:
            abort(400)

        user.name = name
        user.surname = surname

        db.session.add(user)
        db.session.commit()

        return dict(id=user.id,
                    name=user.name,
                    surname=user.surname)

    @staticmethod
    def delete(id):

        if not id:
            abort(400)

        User.query.filter(User.id == id).delete()
        db.session.commit()

    @staticmethod
    def find_one(id):
        user = User.query.filter_by(id=id).first()
        if not user:
            abort(404)

        return dict(id=user.id, name=user.name, surname=str(user.surname))
