from flask import jsonify
from flask_smorest import abort

from backend.storages.db import users, currencies
from backend.utils.utils import contains


class UsersManagerStorage:
    def add(self, user_data):
        if contains(users.get_users(), "user_name", user_data["user_name"]):
            abort(400, message="User with that name already exists!")
        if not contains(currencies.get_currencies(), "currency_id", user_data["user_currency"]):
            abort(404, message="Can only add existing currency to user!")
        return jsonify(users.add(user_data))

    def get_users(self):
        return jsonify(users.get_users())

    def get_user_by_id(self, user_id):
        selected = users.get_user_by_id(user_id)
        if not selected:
            abort(404, message="User does not exist!")
        return jsonify(selected[0])

    def set_user_currency(self, user_data, user_id):
        if not contains(currencies.get_currencies(), "currency_id", user_data["user_currency"]):
            abort(404, "Can only add existing currency to user!")
        selected = users.set_user_currency(
            user_id, user_data["user_currency"]
        )
        if not selected:
            abort(404, message="User does not exist!")
        return jsonify(selected[0])
