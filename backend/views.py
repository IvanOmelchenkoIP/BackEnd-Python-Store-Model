import os

from flask import jsonify
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
    db.create_all()

api.register_blueprint(CurrencyBlueprint)
api.register_blueprint(UsersBlueprint)
api.register_blueprint(RecordsBlueprint)
api.register_blueprint(CategoriesBlueprint)
