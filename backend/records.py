import uuid
import datetime

class Records:
    def __init__(self):
        self.records = []

    def add(self, record_data):
        record_id = uuid.uuid4()
        record_time = datetime.now()
        record = {
            "record_id": record_id, 
            "user_id": record_data["user_id"], 
            "category_id": record_data["category_id"], 
            "time": record_time, 
            "sum": record_data["sum"]
        }
        self.records.append(record)
        return record