import uuid
from datetime import datetime

from backend.utils.utils import select


class RecordsStorage:
    def __init__(self):
        self.records = []

    def add(self, record_data, users):
        record = {
            "record_id": uuid.uuid4().int,
            "record_time": datetime.now(),
            **record_data
        }
        if "record_currency" not in record:
            record["record_currency"] = select(
                users, "user_id", record["user_id"]
            )[0]["user_currency"]
        self.records.append(record)
        return record

    def get_records(self, user_id, category_id):
        if user_id == None:
            return self.records
        selected = select(self.records, "user_id", user_id)
        if category_id:
            selected = select(selected, "category_id", category_id)
        return selected

    def get_record_by_id(self, record_id):
        return select(self.records, "record_id", record_id)
