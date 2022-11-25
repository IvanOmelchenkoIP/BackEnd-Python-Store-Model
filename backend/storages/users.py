import uuid


class UsersStorage:
    def __init__(self):
        self.users = []

    def add(self, user_data):
        user = {
            "user_id": uuid.uuid4().int,
            **user_data
        }
        self.users.append(user)
        return user

    def get_users(self):
        return self.users
