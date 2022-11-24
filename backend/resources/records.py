from flask import MethodView, jsonify, request
from flask_smorest import Blueprint, abort

from backend.storages import categories, users, records

blp = Blueprint("records", __name__, description = "Blueprint for operations on records")

@blp.route("/category")
class Records(MethodView):
    def post(self):
        user_list = users.get_users()
        category_list = categories.get_categories()
        record_res = records.add(request.get_json(), user_list, category_list)
        if "err" in record_res:
            abort(400, record_res["err"])
        res = {"status": "OK", "record": record_res}
        return jsonify(res)

    def get(self):
        user_id = request.args.get("user_id")
        category_id = request.args.get("category_id")
        return jsonify(records.get_records(user_id, category_id))