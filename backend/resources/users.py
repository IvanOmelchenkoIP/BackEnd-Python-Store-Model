from flask.views import MethodView
from flask import jsonify
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import IntegrityError

from backend.models.db import db
from backend.models.users import UserModel

from backend.storages.storages import users
from backend.resources.schemas import UserSchema
from backend.utils.utils import contains

blp = Blueprint(
    "user", __name__, description="Blueprint for operations on users"
)


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
        except IntegrityError:
            abort(404, message="User with that name already exists!")
        return user

    @blp.response(200, UserSchema(many=True))
    def get(self):
        return jsonify(users.get_users())
