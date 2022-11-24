import uuid
from datetime import datetime

from backend.utils.utils import contains, select


class RecordsStorage:
    def __init__(self):
        self.records = []

    def add(self, record_data, users, categories):
        record_id = uuid.uuid4().int
        user_id = record_data["user_id"]
        category_id = record_data["category_id"]
        record_time = datetime.now()
        record_sum = record_data["record_sum"]

        if user_id == None or category_id == None or record_sum == None:
            return {"err": "When creating a new record, user_id, category_id and record_sum must be specified!"}
        if contains(users, "user_id", user_id) == False:
            return {"err": "Can only add record for existing users with user_id!"}
        if contains(categories, "category_id", category_id) == False:
            return {"err": "Can only add record for existing category with category_id!"}

        record = {
            "record_id": record_id,
            "user_id": user_id,
            "category_id": category_id,
            "record_time": record_time,
            "record_sum": record_sum
        }

        self.records.append(record)
        return record

    def get_records(self, user_id, category_id):
        if user_id == None:
            return self.records

        attribute = "user_id"
        user_records = select(self.records, attribute, user_id)
        if category_id == None:
            return user_records

        attribute = "category_id"
        category_records = select(self.records, attribute, category_id)
        return category_records
