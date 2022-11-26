from flask import jsonify

from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import IntegrityError

from backend.models.db import db
from backend.models.currencies import CurrencyModel

from backend.resources.schemas import CurrencySchema

from backend.storages.storages import currencies
from backend.utils.utils import contains

blp = Blueprint(
    "currency", __name__, description="Blueprint for operations on currencies"
)


@blp.route("/currency/<string:currency_id>")
class Currency(MethodView):
    @blp.response(200, CurrencySchema)
    def get(self, currency_id):
        #selected = currencies.get_currency_by_id(currency_id)
        # if not selected:
        #    abort(404, selected="Currency does not exist!")
        # return jsonify(selected[0])
        return CurrencyModel.query.get_or_404(currency_id)


@blp.route("/currency")
class Currency(MethodView):
    @blp.arguments(CurrencySchema)
    @blp.response(200, CurrencySchema)
    def post(self, currency_data):
        # if contains(currencies.get_currencies(), "currency_name", currency_data["currency_name"]):
        #    abort(404, message="The currency already exists!")
        # return jsonify(currencies.add(currency_data))
        currency = CurrencyModel(**currency_data)
        try:
            db.session.add(currency)
            db.session.commit()
        except IntegrityError:
            abort(404, message="The category already exists!")
        return currency

    @blp.response(200, CurrencySchema(many=True))
    def get(self):
        # return jsonify(currencies.get_currencies())
        return CurrencyModel.query.all()
