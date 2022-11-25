#from flask import jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import IntegrityError

from backend.models.db import db
from backend.models.categories import CategoryModel

from backend.resources.schemas import CategorySchema

#from backend.storages.storages import categories
#from backend.utils.utils import contains

blp = Blueprint(
    "category", __name__, description="Blueprint for operations on categories"
)


@blp.route("/category")
class Categories(MethodView):
    @blp.arguments(CategorySchema)
    @blp.response(200, CategorySchema)
    def post(self, category_data):
        # if contains(categories.get_categories(), "category_name", category_data["category_name"]):
        #    abort(404, message="The category already exists!")
        # return jsonify(categories.add(category_data))
        category = CategoryModel(**category_data)
        try:
            db.session.add(category)
            db.session.commit()
        except IntegrityError:
            abort(404, message="The category already exists!")
        return category

    @blp.response(200, CategorySchema(many=True))
    def get(self):
        # return jsonify(categories.get_categories())
        return CategoryModel.query.all()
