from flask import jsonify
from flask_smorest import abort

from backend.data.managers.base import CurrenciesManager

from backend.data.db.storages.db import currencies
from backend.utils.utils import contains


class CurrenciesManagerStorage(CurrenciesManager):
    def add(self, currency_data):
        if contains(currencies.get_currencies(), "currency_name", currency_data["currency_name"]):
            abort(400, message="The currency already exists!")
        return jsonify(currencies.add(currency_data))

    def get_currencies(self):
        return jsonify(currencies.get_currencies())

    def get_currency_by_id(self, currency_id):
        selected = currencies.get_currency_by_id(currency_id)
        if not selected:
            abort(404, selected="Currency does not exist!")
        return jsonify(selected[0])
