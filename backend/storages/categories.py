import uuid


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
