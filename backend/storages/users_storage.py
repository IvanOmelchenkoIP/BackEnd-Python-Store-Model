import uuid


class UsersStorage:
    def __init__(self):
        self.users = []

    def add(self, user_data):
        user_id = uuid.uuid4().int
        user_name = user_data["user_name"]

        if user_name == None:
            return {"err": "When creating new user, user_name must be specified!"}

        user = {
            "user_id": user_id,
            "user_name": user_name
        }
        
        self.users.append(user)
        return user

    def get_users(self):
        return self.users
