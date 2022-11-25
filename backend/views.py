from backend.models.db import db
from flask_smorest import Api
from backend import app

from backend.resources.users import blp as UsersBlueprint
from backend.resources.categories import blp as CategoriesBlueprint
from backend.resources.records import blp as RecordsBlueprint
from backend.resources.currencies import blp as CurrencyBlueprint

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Backend Labs"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.2"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

api = Api(app)

with app.app_context():
    db.create_all()
    #db.drop_all()

api.register_blueprint(UsersBlueprint)
api.register_blueprint(CategoriesBlueprint)
api.register_blueprint(RecordsBlueprint)
api.register_blueprint(CurrencyBlueprint)