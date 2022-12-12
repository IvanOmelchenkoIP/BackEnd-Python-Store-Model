from flask_smorest import abort
from sqlalchemy.exc import IntegrityError

from backend.data.managers.base import CategoriesManager

from backend.data.db.models.db import db
from backend.data.db.models.categories import CategoryModel


class CategoriesManagerORM(CategoriesManager):
    def add(self, category_data):
        category = CategoryModel(**category_data)
        try:
            db.session.add(category)
            db.session.commit()
        except IntegrityError:
            abort(
                400, message="There was an error creating new (category may already exist)!"
            )
        return category

    def get_categories(self):
        return CategoryModel.query.all()

    def get_category_by_id(self, category_id):
        return CategoryModel.query.get_or_404(category_id)
