from flask_jwt_extended import create_access_token
from flask import jsonify
from flask_smorest import abort
from sqlalchemy.exc import IntegrityError
from passlib.hash import pbkdf2_sha256

from backend.models.db import db
from backend.models.users import UserModel
from backend.models.currencies import CurrencyModel


class UsersManagerORM:
    def register(self, user_data):
        if not db.session.scalar(
            CurrencyModel.query.filter_by(
                currency_id=user_data["user_currency"]
            )
        ):
            abort(404, message="Can only add existing currency to user!")
        user = UserModel(
            user_name=user_data["user_name"],
            user_currency=user_data["user_currency"],
            user_password=pbkdf2_sha256.hash(user_data["user_password"])
        )
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            abort(
                400, message="There was an error creating new user (user may already exist)!"
            )
        return user

    def login(self, user_data):
        user = UserModel.query.filter_by(user_name=user_data["user_name"])
        if user and pbkdf2_sha256.verify(user_data["user_password"], user.user_password):
            access_token = create_access_token(identity=user.user_id)
            return jsonify({"user_id": user.user_id, "access_token": access_token})
        else:
            abort(
                400, message="Cannot login: wrong user name or password!"
            )

    def get_users(self):
        return UserModel.query.all()

    def get_user_by_id(self, user_id):
        return UserModel.query.get_or_404(user_id)

    def set_user_currency(self, user_data, user_id):
        if not db.session.scalar(
            CurrencyModel.query.filter_by(
                currency_id=user_data["user_currency"]
            )
        ):
            abort(404, message="Can only add existing currency to user!")
        user = UserModel.query.get_or_404(user_id)
        try:
            user.user_currency = user_data["user_currency"]
            db.session.commit()
        except IntegrityError:
            abort(404, message="Can only add existing currency to user!")
        return user
