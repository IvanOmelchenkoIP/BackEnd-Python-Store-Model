import os

from flask_jwt_extended import JWTManager

from flask import jsonify
from flask_smorest import Api

from backend.data.db.models.db import db
from backend import app

from backend.endpoints.resources.currencies import blp as CurrencyBlueprint
from backend.endpoints.resources.users import blp as UsersBlueprint
from backend.endpoints.resources.categories import blp as CategoriesBlueprint
from backend.endpoints.resources.records import blp as RecordsBlueprint

from backend.data.initial_data.currency import set_initial_currency

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
jwt.init_app(app)


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return (
        jsonify({"message": "The token has expired.", "error": "token_expired"}),
        401,
    )


@jwt.invalid_token_loader
def invalid_token_callback(error):
    return (
        jsonify(
            {"message": "Signature verification failed.", "error": "invalid_token"}
        ),
        401,
    )


@jwt.unauthorized_loader
def missing_token_callback(error):
    return (
        jsonify(
            {
                "description": "Request does not contain an access token.",
                "error": "authorization_required",
            }
        ),
        401,
    )


with app.app_context():
    db.drop_all()
    db.create_all()
    set_initial_currency()

api.register_blueprint(CurrencyBlueprint)
api.register_blueprint(UsersBlueprint)
api.register_blueprint(RecordsBlueprint)
api.register_blueprint(CategoriesBlueprint)
