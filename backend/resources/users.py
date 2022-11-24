from flask.views import MethodView
from flask import jsonify, request
from flask_smorest import Blueprint, abort

from backend.storages.storages import users

blp = Blueprint("user", __name__, description = "Blueprint for operations on users")

@blp.route("/user")
class Users(MethodView):
    def post(self):
        user_res = users.add(request.get_json())
        if "err" in user_res:
            abort(400, user_res["err"])
        res = {"status": "OK", "user": user_res}
        return jsonify(res)

    def get(self):
        return jsonify(users.get_users())
