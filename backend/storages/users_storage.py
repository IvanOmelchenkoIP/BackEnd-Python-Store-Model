import uuid


class UsersStorage:
    def __init__(self):
        self.users = []

    def add(self, user_name):
        user = {
            "user_id": str(uuid.uuid4().int),
            "user_name": user_name
        }
        self.users.append(user)
        return user

    def get_users(self):
        return self.users
