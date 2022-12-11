from backend.data.managers.models.currencies import CurrenciesManagerORM
from backend.data.managers.models.categories import CategoriesManagerORM
from backend.data.managers.models.users import UsersManagerORM, LoginManagerORM
from backend.data.managers.models.records import RecordsManagerORM

currencies_orm = CurrenciesManagerORM()

categories_orm = CategoriesManagerORM()

login_orm = LoginManagerORM()

users_orm = UsersManagerORM()

records_orm = RecordsManagerORM()
