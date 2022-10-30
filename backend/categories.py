import uuid

class Categories:
    def __init__(self):
        self.categories = []

    def add(self, category_data):
        category_id = uuid.uuid4()
        category = {
            "category_id": category_id, 
            "category_name": category_data["category_name"]
            }
        self.users.append(category)
        return category