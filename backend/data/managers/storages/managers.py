from backend.managers.storages.currencies import CurrenciesManagerStorage
from backend.managers.storages.categories import CategoriesManagerStorage
from backend.managers.storages.users import UsersManagerStorage
from backend.managers.storages.records import RecordsManagerStorage

currencies_storage = CurrenciesManagerStorage()

categories_storage = CategoriesManagerStorage()

users_storage = UsersManagerStorage()

records_storage = RecordsManagerStorage()
