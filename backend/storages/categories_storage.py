import uuid


class CategoriesStorage:
    def __init__(self):
        self.categories = []

    def add(self, category_data):
        category_id = uuid.uuid4().int
        category_name = category_data["category_name"]

        if category_name == None: 
            return {"err": "When creating a new category, a category_name must be specified!"}

        category = {
            "category_id": category_id,
            "category_name": category_name
        }

        self.categories.append(category)
        return category

    def get_categories(self):
        return self.categories
