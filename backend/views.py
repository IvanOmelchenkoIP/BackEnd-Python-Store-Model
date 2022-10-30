from flask import jsonify, request

from backend import app
from backend.storages import users, categories, records

@app.post("/newuser")
def create_user():
    user_res = users.add(request.get_json())
    res = {"status": "OK", "user": user_res}
    return jsonify(res)

@app.post("/newcategory")
def create_category():
    category_res = categories.add(request.get_json())
    res = {"status": "OK", "category": category_res}
    return jsonify(res)

@app.post("/newrecord")
def create_record():
    record_res = records.add(request.get_json())
    res = {"status": "OK", "record": record_res}
    return jsonify(res)

@app.route("/categories")
def get_categories():
    return jsonify(categories.get_categories())

@app.route("/records")
def get_records():
    return jsonify(records)