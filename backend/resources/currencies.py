from flask.views import MethodView
from flask_smorest import Blueprint

from backend.schemas.schemas import CurrencySchema

from backend.managers.storages.managers import currencies_storage
from backend.managers.models.managers import currencies_orm

blp = Blueprint(
    "currency", __name__, description="Blueprint for operations on currencies"
)


@blp.route("/currency/<string:currency_id>")
class Currency(MethodView):
    @blp.response(200, CurrencySchema)
    def get(self, currency_id):
        #currency = currencies_storage.get_currency_by_id(currency_id)
        currency = currencies_orm.get_currency_by_id(currency_id)
        return currency


@blp.route("/currency")
class Currency(MethodView):
    @blp.arguments(CurrencySchema)
    @blp.response(200, CurrencySchema)
    def post(self, currency_data):
        #currency = currencies_storage.add(currency_data)
        currency = currencies_orm.add(currency_data)
        return currency

    @blp.response(200, CurrencySchema(many=True))
    def get(self):
        #currencies = currencies_storage.get_currencies()
        currencies = currencies_orm.get_currencies()
        return currencies
