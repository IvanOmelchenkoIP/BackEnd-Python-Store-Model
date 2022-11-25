import uuid
from datetime import datetime

from backend.utils.utils import select


class RecordsStorage:
    def __init__(self):
        self.records = []

    def add(self, record_data):
        record = {
            "record_id": uuid.uuid4().int,
            "record_time": datetime.now(),
            **record_data
        }
        self.records.append(record)
        return record

    def get_records(self, user_id, category_id):
        if user_id == None:
            return self.records
        selected = select(self.records, "user_id", user_id)
        if category_id:
            selected = select(selected, "category_id", category_id)
        return selected