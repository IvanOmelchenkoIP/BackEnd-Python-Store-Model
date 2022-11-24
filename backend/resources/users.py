from flask.views import MethodView
from flask import jsonify, request
from flask_smorest import Blueprint, abort

from backend.storages.storages import users

from backend.resources.schemas import UserSchema

blp = Blueprint(
    "user", __name__,
    description="For operations on users"
)


@blp.route("/user")
class Users(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        user_name = user_data["user_name"]
        user_res = users.add(user_name)
        return jsonify({"status": "OK", "user": user_res})

    def get(self):
        return jsonify(users.get_users())
