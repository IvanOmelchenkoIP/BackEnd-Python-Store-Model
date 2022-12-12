from flask_smorest import abort

#from backend.data.managers.storages.managers import currencies_manager
from backend.data.managers.models.managers import currencies_manager


def set_initial_currency():
    initial_currency = {"currency_name": "Hryvnia"}
    currency = currencies_manager.add(initial_currency)
    return currency
