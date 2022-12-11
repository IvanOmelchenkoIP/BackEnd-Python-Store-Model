from flask import jsonify
from flask_smorest import abort

from backend.data.managers.base import CategoriesManager

from backend.data.db.storages.db import categories
from backend.utils.utils import contains


class CategoriesManagerStorage(CategoriesManager):
    def add(self, category_data):
        if contains(categories.get_categories(), "category_name", category_data["category_name"]):
            abort(400, message="The category already exists!")
        return jsonify(categories.add(category_data))

    def get_categories(self):
        return jsonify(categories.get_categories())

    def get_category_by_id(self, category_id):
        selected = categories.get_category_by_id(category_id)
        if not selected:
            abort(404, message="Category does not exist!")
        return jsonify(selected[0])
