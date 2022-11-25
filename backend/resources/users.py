# from flask import jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import IntegrityError

from backend.models.db import db
from backend.models.users import UserModel

from backend.resources.schemas import UserSchema, UserCurrencySchema

# from backend.storages.storages import users
# from backend.utils.utils import contains

blp = Blueprint(
    "user", __name__, description="Blueprint for operations on users"
)


@blp.route("/user/<string:user_id>")
class User(MethodView):
    @blp.response(200, UserSchema)
    def get(self, user_id):
        return UserModel.query.get_or_404(user_id)

    @blp.arguments(UserCurrencySchema)
    @blp.response(200, UserSchema)
    def post(self, user_data, user_id):
        user = UserModel.query.get_or_404(user_id)
        try:
            user.user_currency = user_data.get("user_currency")
            db.session.commit()
        except IntegrityError:
            abort(404, message="Error occured updating user default currency!")
        return user


@blp.route("/user")
class Users(MethodView):
    @blp.arguments(UserSchema)
    @blp.response(200, UserSchema)
    def post(self, user_data):
        # if contains(users.get_users(), "user_name", user_data["user_name"]):
        #    abort(404, message="User with that name already exists!")
        # return jsonify(users.add(user_data))
        user = UserModel(**user_data)
        try:
            db.session.add(user)
            db.session.commit()
            print(user.user_id, user.user_name)
        except IntegrityError:
            abort(404, message="User with that name already exists!")
        return user

    @blp.response(200, UserSchema(many=True))
    def get(self):
        # return jsonify(users.get_users())
        return UserModel.query.all()
