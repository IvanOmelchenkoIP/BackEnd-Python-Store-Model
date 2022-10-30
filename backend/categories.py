import uuid


class Categories:
    def __init__(self):
        self.categories = []

    def add(self, category_data):
        category_id = uuid.uuid4().int
        category_name = category_data["category_name"]

        category = {
            "category_id": category_id,
            "category_name": category_name
        }

        self.categories.append(category)
        return category

    def get_categories(self):
        return self.categories
