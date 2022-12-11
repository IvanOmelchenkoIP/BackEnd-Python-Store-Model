from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint

from backend.views.schemas.schemas import CategorySchema

#from backend.data.managers.storages.managers import categories_manager
from backend.data.managers.models.managers import categories_manager

blp = Blueprint(
    "category", __name__, description="Blueprint for operations on categories"
)


@blp.route("/category/<string:category_id>")
class Category(MethodView):
    @blp.response(200, CategorySchema)
    @jwt_required()
    def get(self, category_id):
        category = categories_manager.get_category_by_id(category_id)
        return category


@blp.route("/category")
class Categories(MethodView):
    @blp.arguments(CategorySchema)
    @blp.response(200, CategorySchema)
    @jwt_required()
    def post(self, category_data):
        category = categories_manager.add(category_data)
        return category

    @blp.response(200, CategorySchema(many=True))
    @jwt_required()
    def get(self):
        categories = categories_manager.get_categories()
        return categories
