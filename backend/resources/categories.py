from flask.views import MethodView
from flask import jsonify, request
from flask_smorest import Blueprint, abort

from backend.storages.storages import categories

from backend.resources.schemas import CategorySchema

blp = Blueprint("category", __name__,
                description="Blueprint for operations on categories")


@blp.route("/category")
class Categories(MethodView):
    @blp.arguments(CategorySchema)
    def post(self, category_data):
        category_name = category_data["category_name"]
        category_res = categories.add(category_name)
        return jsonify({"status": "OK", "user": category_res})

    def get(self):
        return jsonify(categories.get_users())
