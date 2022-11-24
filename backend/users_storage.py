import uuid


class UsersStorage:
    def __init__(self):
        self.users = []

    def add(self, user_data):
        user_id = uuid.uuid4().int
        user_name = user_data["user_name"]

        user = {
            "user_id": user_id,
            "user_name": user_name
        }
        
        self.users.append(user)
        return user

    def get_users(self):
        return self.users
