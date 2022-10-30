import uuid

class Users:
    def __init__(self):
        self.users = []

    def add(self, user_data):
        user_id = uuid.uuid4()
        user = {
            "user_id": user_id, 
            "user_name": user_data["user_name"]
            }
        self.users.append(user)
        return user