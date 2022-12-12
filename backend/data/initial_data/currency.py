from flask_smorest import abort

#from backend.data.managers.storages.managers import currencies_manager
from backend.data.managers.models.managers import currencies_manager

initial_currency = {"currency_name": "Hryvnya"}


def set_initial_currency():
    currency = currencies_manager.add(initial_currency)
    return currency
