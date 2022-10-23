import uuid
import datetime

class Records:
    def __init__(self):
        self.records = []

    def add(self, user_data):
        data = user_data
        record_id = uuid.uuid4()
        time = datetime.now()
        record = {
            "record_id": record_id, 
            "user_id": data["user_id"], 
            "category_id": data["category_id"], 
            "time": time, 
            "sum": data["sum"]
        }
        self.records.append(record)
        return record