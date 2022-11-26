import uuid

from backend.utils.utils import select


class CategoriesStorage:
    def __init__(self):
        self.categories = []

    def add(self, category_data):
        category = {
            "category_id": uuid.uuid4().int,
            **category_data
        }
        self.categories.append(category)
        return category

    def get_categories(self):
        return self.categories

    def get_category_by_id(self, category_id):
        return select(self.categories, "category_id", category_id)
