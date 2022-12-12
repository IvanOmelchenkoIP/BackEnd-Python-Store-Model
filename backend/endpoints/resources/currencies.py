from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint

from backend.endpoints.schemas.schemas import CurrencySchema

#from backend.data.managers.storages.managers import currencies_manager
from backend.data.managers.models.managers import currencies_manager

blp = Blueprint(
    "currency", __name__, description="Blueprint for operations on currencies"
)


@blp.route("/currency/<string:currency_id>")
class Currency(MethodView):
    @blp.response(200, CurrencySchema)
    @jwt_required()
    def get(self, currency_id):
        currency = currencies_manager.get_currency_by_id(currency_id)
        return currency


@blp.route("/currency")
class Currency(MethodView):
    @blp.arguments(CurrencySchema)
    @blp.response(200, CurrencySchema)
    @jwt_required()
    def post(self, currency_data):
        currency = currencies_manager.add(currency_data)
        return currency

    @blp.response(200, CurrencySchema(many=True))
    @jwt_required(optional=True)
    def get(self):
        currencies = currencies_manager.get_currencies()
        return currencies
