import uuid
from datetime import datetime

from backend.utils.utils import select


class RecordsStorage:
    def __init__(self):
        self.records = []

    def add(self, user_id, category_id, record_sum):
        record = {
            "record_id": str(uuid.uuid4().int),
            "user_id": user_id,
            "category_id": category_id,
            "record_time": datetime.now(),
            "record_sum": record_sum
        }
        self.records.append(record)
        return record

    def get_records(self, user_id, category_id):
        if user_id == None:
            return self.records

        user_records = select(self.records, "user_id", user_id)
        if category_id == None:
            return user_records
        category_records = select(self.records, "category_id", category_id)
        return category_records
