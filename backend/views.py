from flask import abort
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
    user_list = users.get_users()
    category_list = categories.get_categories()
    record_res = records.add(request.get_json(), user_list, category_list)
    if "err" in record_res:
        abort(400, record_res["err"])
    res = {"status": "OK", "record": record_res}
    return jsonify(res)


@app.route("/users")
def get_users():
    return jsonify(users.get_users())


@app.route("/categories")
def get_categories():
    return jsonify(categories.get_categories())


@app.route("/records")
def get_records():
    user_id = request.args.get("user_id")
    category_id = request.args.get("category_id")
    return jsonify(records.get_records(user_id, category_id))
