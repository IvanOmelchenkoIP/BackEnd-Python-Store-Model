#from flask import abort
#from flask import jsonify, request
from flask_smorest import Api
from backend import app
#from backend.storages.storages import users, categories, records

from backend.resources.users import blp as UsersBlueprint
from backend.resources.categories import blp as CategoriesBlueprint
from backend.resources.records import blp as RecordsBlueprint

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Backend Labs"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.2"

api = Api(app)
api.register_blueprint(UsersBlueprint)
api.register_blueprint(CategoriesBlueprint)
api.register_blueprint(RecordsBlueprint)