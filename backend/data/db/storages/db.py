from backend.data.db.storages.currencies import CurrenciesStorage
from backend.data.db.storages.users import UsersStorage
from backend.data.db.storages.categories import CategoriesStorage
from backend.data.db.storages.records import RecordsStorage

currencies = CurrenciesStorage()

users = UsersStorage()

categories = CategoriesStorage()

records = RecordsStorage()
