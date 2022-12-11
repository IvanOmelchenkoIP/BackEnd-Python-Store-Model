from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint

from backend.views.schemas.schemas import UserSchema, UserCurrencySchema, UserLoginSchema, UserTokenSchema

from backend.data.managers.storages.managers import users_storage
from backend.data.managers.models.managers import users_orm, login_orm

blp = Blueprint(
    "user", __name__, description="Blueprint for operations on users"
)


@blp.route("/register")
class UserResistrator(MethodView):
    @blp.arguments(UserSchema)
    @blp.response(200, UserSchema)
    def post(self, user_data):
        #user = users_storage.add(user_data)
        user = login_orm.register(user_data)
        return user


@blp.route("/login")
class UserLogin(MethodView):
    @blp.arguments(UserLoginSchema)
    @blp.response(200, UserTokenSchema)
    def post(self, user_data):
        access_token = login_orm.login(user_data)
        return access_token


@blp.route("/user/<string:user_id>")
class User(MethodView):
    @blp.response(200, UserSchema)
    @jwt_required()
    def get(self, user_id):
        #user = users_storage.get_user_by_id(user_id)
        user = users_orm.get_user_by_id(user_id)
        return user

    @blp.arguments(UserCurrencySchema)
    @blp.response(200, UserSchema)
    @jwt_required()
    def post(self, user_data, user_id):
        #user = users_storage.set_user_currency(user_data, user_id)
        user = users_orm.set_user_currency(user_data, user_id)
        return user


@blp.route("/users")
class Users(MethodView):
    @blp.response(200, UserSchema(many=True))
    @jwt_required()
    def get(self):
        #users = users_storage.get_users()
        users = users_orm.get_users()
        return users
