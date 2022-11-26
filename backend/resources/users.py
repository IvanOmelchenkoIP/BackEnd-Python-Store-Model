from flask import jsonify

from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import IntegrityError

from backend.models.db import db
from backend.models.users import UserModel

from backend.resources.schemas import UserSchema, UserCurrencySchema

from backend.storages.storages import users, currencies
from backend.utils.utils import contains

blp = Blueprint(
    "user", __name__, description="Blueprint for operations on users"
)


@blp.route("/user/<string:user_id>")
class User(MethodView):
    @blp.response(200, UserSchema)
    def get(self, user_id):
        #selected = users.get_user_by_id(user_id)
        # if not selected:
        #    abort(404, message="User does not exist!")
        # return jsonify(selected[0])
        return UserModel.query.get_or_404(user_id)

    @blp.arguments(UserCurrencySchema)
    @blp.response(200, UserSchema)
    def post(self, user_data, user_id):
        # if not contains(currencies.get_currencies(), "currency_id", user_data["user_currency"]):
        #    abort(404, "Can only add existing currency to user!")
        # selected = users.set_user_currency(
        #    user_id, user_data["user_currency"]
        # )
        # if not selected:
        #    abort(404, message="User does not exist!")
        # return jsonify(selected[0])
        user = UserModel.query.get_or_404(user_id)
        try:
            user.user_currency = user_data.get("user_currency")
            db.session.commit()
        except IntegrityError:
            abort(404, message="Error occured updating user default currency!")
        return user


@ blp.route("/user")
class Users(MethodView):
    @ blp.arguments(UserSchema)
    @ blp.response(200, UserSchema)
    def post(self, user_data):
        # if contains(users.get_users(), "user_name", user_data["user_name"]):
        #    abort(404, message="User with that name already exists!")
        # if "user_currency" in user_data:
        #    if not contains(currencies.get_currencies(), "currency_id", user_data["user_currency"]):
        #        abort(404, message="Can only add existing currency to user!")
        # return jsonify(users.add(user_data))
        user = UserModel(**user_data)
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            abort(404, message="User with that name already exists!")
        return user

    @ blp.response(200, UserSchema(many=True))
    def get(self):
        # return jsonify(users.get_users())
        return UserModel.query.all()
