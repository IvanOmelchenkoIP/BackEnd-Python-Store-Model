from backend.data.managers.storages.currencies import CurrenciesManagerStorage
from backend.data.managers.storages.categories import CategoriesManagerStorage
from backend.data.managers.storages.users import UsersManagerStorage, LoginManagerStorage
from backend.data.managers.storages.records import RecordsManagerStorage

currencies_manager = CurrenciesManagerStorage()

categories_manager = CategoriesManagerStorage()

login_manager = LoginManagerStorage()

users_manager = UsersManagerStorage()

records_manager = RecordsManagerStorage()
