from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint

from backend.endpoints.schemas.schemas import UserSchema, UserCurrencySchema, UserLoginSchema, UserTokenSchema

from backend.data.managers.storages.managers import users_manager, login_manager
#from backend.data.managers.models.managers import login_manager, users_manager

blp = Blueprint(
    "user", __name__, description="Blueprint for operations on users"
)


@blp.route("/register")
class UserResistrator(MethodView):
    @blp.arguments(UserSchema)
    @blp.response(200, UserSchema)
    def post(self, user_data):
        user = login_manager.register(user_data)
        return user


@blp.route("/login")
class UserLogin(MethodView):
    @blp.arguments(UserLoginSchema)
    @blp.response(200, UserTokenSchema)
    def post(self, user_data):
        access_token = login_manager.login(user_data)
        return access_token


@blp.route("/user/<string:user_id>")
class User(MethodView):
    @blp.response(200, UserSchema)
    @jwt_required()
    def get(self, user_id):
        user = users_manager.get_user_by_id(user_id)
        return user

    @blp.arguments(UserCurrencySchema)
    @blp.response(200, UserSchema)
    @jwt_required()
    def post(self, user_data, user_id):
        user = users_manager.set_user_currency(user_data, user_id)
        return user


@blp.route("/users")
class Users(MethodView):
    @blp.response(200, UserSchema(many=True))
    @jwt_required()
    def get(self):
        users = users_manager.get_users()
        return users
