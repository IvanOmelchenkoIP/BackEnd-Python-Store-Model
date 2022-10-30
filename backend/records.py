import uuid
from datetime import datetime

from backend.utils import select


class Records:
    def __init__(self):
        self.records = []

    def add(self, record_data):
        record_id = uuid.uuid4().int
        user_id = record_data["user_id"]
        category_id = record_data["category_id"]
        record_time = datetime.now()
        record_sum = record_data["record_sum"]

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
