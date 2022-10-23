from flask import jsonify, request
from backend import app

users = []
categories = []
records = []

@app.post("/newuser")
def create_user():
    user_data = request.get_json()
    users.append(user_data)
    return "OK"

@app.post("/newcategory")
def create_category():
    category_data = request.get_json()
    categories.append(category_data)
    return "OK"

@app.post("/newrecord")
def create_record():
    record_data = request.get_json()
    records.append(record_data)
    return "OK"

@app.route("/categories")
def get_categories():
    return jsonify(categories)

@app.route("/userrecords")
def get_records_by_user():
    return jsonify(records)

@app.route("/categoryrecords")
def get_records_by_category():
    return jsonify(records)