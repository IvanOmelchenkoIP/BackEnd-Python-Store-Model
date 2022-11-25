from flask.views import MethodView
from flask import jsonify
from flask_smorest import Blueprint, abort

from backend.storages.storages import categories
from backend.resources.schemas import CategorySchema
from backend.utils.utils import contains

blp = Blueprint(
    "category", __name__, description="Blueprint for operations on categories"
)


@blp.route("/category")
class Categories(MethodView):
    @blp.arguments(CategorySchema)
    @blp.response(200, CategorySchema)
    def post(self, category_data):
        if contains(categories.get_categories(), "category_name", category_data["category_name"]):
            abort(404, message="The category already exists!")
        return jsonify(categories.add(category_data))

    @blp.response(200, CategorySchema(many=True))
    def get(self):
        return jsonify(categories.get_categories())
