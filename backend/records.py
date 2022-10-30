import uuid
from datetime import datetime

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
            "record_time": record_time, 
            "record_sum": record_data["record_sum"]
        }
        self.records.append(record)
        return record

    def get_records(self, user_id, category_id):
        if user_id == None:
            return self.records
        
        selected_by_user = []
        for element in self.records:
            print(element)
            if element["user_id"] == user_id:
                selected_by_user.append(element)

        return selected_by_user