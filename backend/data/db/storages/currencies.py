import uuid

from backend.utils.utils import select


class CurrenciesStorage:
    def __init__(self):
        self.currencies = []

    def add(self, currency_data):
        currency = {
            "currency_id": uuid.uuid4().int,
            **currency_data
        }
        self.currencies.append(currency)
        return currency

    def get_currencies(self):
        return self.currencies

    def get_currency_by_id(self, currency_id):
        return select(self.currencies, "currency_id", currency_id)
