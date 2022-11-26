from flask.views import MethodView
from flask_smorest import Blueprint

from backend.schemas.schemas import UserSchema, UserCurrencySchema

from backend.managers.storages.managers import users_storage
from backend.managers.models.managers import users_orm

blp = Blueprint(
    "user", __name__, description="Blueprint for operations on users"
)


@blp.route("/user/<string:user_id>")
class User(MethodView):
    @blp.response(200, UserSchema)
    def get(self, user_id):
        #user = users_storage.get_user_by_id(user_id)
        user = users_orm.get_user_by_id(user_id)
        return user

    @blp.arguments(UserCurrencySchema)
    @blp.response(200, UserSchema)
    def post(self, user_data, user_id):
        #user = users_storage.set_user_currency(user_data, user_id)
        user = users_orm.set_user_currency(user_data, user_id)
        return user


@ blp.route("/user")
class Users(MethodView):
    @ blp.arguments(UserSchema)
    @ blp.response(200, UserSchema)
    def post(self, user_data):
        #user = users_storage.add(user_data)
        user = users_orm.add(user_data)
        return user

    @ blp.response(200, UserSchema(many=True))
    def get(self):
        #users = users_storage.get_users()
        users = users_orm.get_users()
        return users
