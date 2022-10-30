import uuid
from datetime import datetime

class Records:
    def __init__(self):
        self.records = []

    def add(self, record_data):
        record_id = uuid.uuid4().int
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
        if user_id == None: return self.records 
        
        user_records = []
        for element in self.records:
            if int(element["user_id"]) == int(user_id):
                user_records.append(element)

        if category_id == None: return user_records 

        category_records = []
        for element in self.records:
            if int(element["category_id"]) == int(category_id):
                category_records.append(element)

        return category_records