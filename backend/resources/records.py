from flask.views import MethodView
from flask import jsonify, request
from flask_smorest import Blueprint, abort

from backend.storages.storages import categories, users, records
from backend.resources.schemas import RecordSchema
from backend.utils.utils import contains

blp = Blueprint("records", __name__,
                description="Blueprint for operations on records")


@blp.route("/category")
class Records(MethodView):
    @blp.arguments(RecordSchema)
    def post(self, record_data):
        user_id = record_data["user_id"]
        category_id = record_data["category_id"]
        record_sum = record_data["record_sum"]
        if contains(users.get_users(), "user_id", user_id) == False:
            abort(404, message="Can only add record for existing user_id!")
        if contains(categories.get_categories(), "category_id", category_id) == False:
            abort(404, message="Can only add record for existing category_id!")

        record_res = records.add(user_id, category_id, record_sum)
        return jsonify({"status": "OK", "record": record_res})

    def get(self):
        user_id = request.args.get("user_id")
        category_id = request.args.get("category_id")
        return jsonify(records.get_records(user_id, category_id))
