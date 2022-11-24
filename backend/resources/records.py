from flask.views import MethodView
from flask import jsonify, request
from flask_smorest import Blueprint, abort

from backend.storages.storages import categories, users, records
from backend.resources.schemas import RecordSchema, RecordRequestSchema
from backend.utils.utils import contains

blp = Blueprint(
    "record", __name__,
    description="Blueprint for operations on records"
)


@blp.route("/record")
class Records(MethodView):
    @blp.arguments(RecordSchema)
    @blp.response(200, RecordRequestSchema)
    def post(self, record_data):
        user_id = record_data["user_id"]
        category_id = record_data["category_id"]
        record_sum = record_data["record_sum"]
        if not contains(users.get_users(), "user_id", user_id):
            abort(404, message="Can only add record for existing user_id!")
        if not contains(categories.get_categories(), "category_id", category_id):
            abort(404, message="Can only add record for existing category_id!")

        record_res = records.add(user_id, category_id, record_sum)
        return jsonify(record_res)

    @blp.arguments(RecordRequestSchema, location="query", as_kwargs=True)
    @blp.response(200, RecordRequestSchema(many=True))
    def get(self, **kwargs):
        print(kwargs.get("user_id"), kwargs.get("category_id"), jsonify(records.get_records(kwargs.get("user_id"), kwargs.get("category_id"))))
        return jsonify(records.get_records(kwargs.get("user_id"), kwargs.get("category_id")))
