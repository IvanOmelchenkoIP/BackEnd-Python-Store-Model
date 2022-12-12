from flask import Flask

import os

from flask_smorest import Api

from backend.data.db.models.db import db

from backend.endpoints.resources.currencies import blp as CurrencyBlueprint
from backend.endpoints.resources.users import blp as UsersBlueprint
from backend.endpoints.resources.categories import blp as CategoriesBlueprint
from backend.endpoints.resources.records import blp as RecordsBlueprint

from backend.data.initial_data.currency import set_initial_currency


def create_app():
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Backend Labs"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.2"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

    db.init_app(app)

    api = Api(app)

    with app.app_context():
        db.drop_all()
        db.create_all()
        set_initial_currency()

    api.register_blueprint(CurrencyBlueprint)
    api.register_blueprint(UsersBlueprint)
    api.register_blueprint(RecordsBlueprint)
    api.register_blueprint(CategoriesBlueprint)

    return app
