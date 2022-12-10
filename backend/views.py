import os

from flask_jwt_extended import JWTManager
from backend.models.db import db
from flask_smorest import Api
from backend import app

from backend.resources.currencies import blp as CurrencyBlueprint
from backend.resources.users import blp as UsersBlueprint
from backend.resources.categories import blp as CategoriesBlueprint
from backend.resources.records import blp as RecordsBlueprint

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Backend Labs"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.2"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

db.init_app(app)

api = Api(app)

jwt = JWTManager(app)

with app.app_context():
    db.create_all()

api.register_blueprint(CurrencyBlueprint)
api.register_blueprint(UsersBlueprint)
api.register_blueprint(RecordsBlueprint)
api.register_blueprint(CategoriesBlueprint)
