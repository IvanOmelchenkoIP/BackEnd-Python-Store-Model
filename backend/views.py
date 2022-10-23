from datetime import datetime
import uuid

from flask import jsonify, request

from backend import app
from backend.users import Users

records = []
categories = []

users = Users()

@app.post("/newuser")
def create_user():
    user_res = users.add(request.get_json())
    res = {"status": "OK", "user": user_res}
    return jsonify(res)

@app.post("/newcategory")
def create_category():
    category_data = request.get_json()
    category_id = uuid.uuid4()
    category = {
        "category_id": category_id, 
        "category_name": category_data["category_name"]
        }
    categories.append(category)
    res = {"status": "OK", "category": category}
    return jsonify(res)

@app.post("/newrecord")
def create_record():
    record_data = request.get_json()
    record_id = uuid.uuid4()
    time = datetime.now()
    record = {
        "record_id": record_id, 
        "user_id": record_data["user_id"], 
        "category_id": record_data["category_id"], 
        "time": time, 
        "sum": record_data["sum"]
        }
    records.append(record)
    res = {"status": "OK", "record": record}
    return jsonify(res)

@app.route("/categories")
def get_categories():
    return jsonify(categories)

@app.route("/userrecords")
def get_records_by_user():
    return jsonify(records)

@app.route("/categoryrecords")
def get_records_by_category():
    return jsonify(records)