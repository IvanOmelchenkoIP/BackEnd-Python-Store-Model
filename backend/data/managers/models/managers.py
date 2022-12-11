from backend.data.managers.models.currencies import CurrenciesManagerORM
from backend.data.managers.models.categories import CategoriesManagerORM
from backend.data.managers.models.users import UsersManagerORM, LoginManagerORM
from backend.data.managers.models.records import RecordsManagerORM

currencies_manager = CurrenciesManagerORM()

categories_manager = CategoriesManagerORM()

login_manager = LoginManagerORM()

users_manager = UsersManagerORM()

records_manager = RecordsManagerORM()
