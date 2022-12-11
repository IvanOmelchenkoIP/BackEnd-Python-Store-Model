from flask_smorest import abort
from sqlalchemy.exc import IntegrityError

from backend.data.managers.base import CurrenciesManager

from backend.data.db.models.db import db
from backend.data.db.models.currencies import CurrencyModel


class CurrenciesManagerORM(CurrenciesManager):
    def add(self, currency_data):
        currency = CurrencyModel(**currency_data)
        try:
            db.session.add(currency)
            db.session.commit()
        except IntegrityError:
            abort(
                400, message="There was an error creating a new currecy (currency may already exist)!"
            )
        return currency

    def get_currencies(self):
        return CurrencyModel.query.all()

    def get_currency_by_id(self, currency_id):
        return CurrencyModel.query.get_or_404(currency_id)
