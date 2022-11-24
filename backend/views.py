from flask import abort
from flask import jsonify, request
from flask_smorest import Api
from backend import app
from backend.storages import users, categories, records

from resources.users import blp as UsersBlueprint
from resources.categories import blp as CategoriesBlueprint
from resources.records import blp as RecordsBlueprint

api = Api(app)

api.config["PROPAGATE_EXCEPTIONS"] = True
api.config["API_TITLE"] = "Backend Labs"
api.config["API_VERSION"] = "v1"

api.register_blueprint(UsersBlueprint)
api.register_blueprint(CategoriesBlueprint)
api.register_blueprint(RecordsBlueprint)


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
