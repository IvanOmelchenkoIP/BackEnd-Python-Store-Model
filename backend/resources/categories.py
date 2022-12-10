from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint

from backend.schemas.schemas import CategorySchema

from backend.managers.storages.managers import categories_storage
from backend.managers.models.managers import categories_orm

blp = Blueprint(
    "category", __name__, description="Blueprint for operations on categories"
)


@blp.route("/category/<string:category_id>")
@jwt_required()
class Category(MethodView):
    @blp.response(200, CategorySchema)
    def get(self, category_id):
        #category = categories_storage.get_category_by_id(category_id)
        category = categories_orm.get_category_by_id(category_id)
        return category


@blp.route("/category")
@jwt_required()
class Categories(MethodView):
    @blp.arguments(CategorySchema)
    @blp.response(200, CategorySchema)
    def post(self, category_data):
        #category = categories_storage.add(category_data)
        category = categories_orm.add(category_data)
        return category

    @blp.response(200, CategorySchema(many=True))
    def get(self):
        #categories = categories_storage.get_categories()
        categories = categories_orm.get_categories()
        return categories
