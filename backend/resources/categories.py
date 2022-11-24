from flask.views import MethodView
from flask import jsonify, request
from flask_smorest import Blueprint, abort

from backend.storages.storages import categories

blp = Blueprint("category", __name__,
                description="Blueprint for operations on categories")


@blp.route("/category")
class Categories(MethodView):
    def post(self):
        category_res = categories.add(request.get_json())
        if "err" in category_res:
            abort(400, category_res["err"])
        res = {"status": "OK", "user": category_res}
        return jsonify(res)

    def get(self):
        return jsonify(categories.get_users())
