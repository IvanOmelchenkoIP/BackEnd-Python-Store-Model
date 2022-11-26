from backend.managers.models.currencies import CurrenciesManagerORM
from backend.managers.models.categories import CategoriesManagerORM
from backend.managers.models.users import UsersManagerORM
from backend.managers.models.records import RecordsManagerORM

currencies_orm = CurrenciesManagerORM()

categories_orm = CategoriesManagerORM()

users_orm = UsersManagerORM()

records_orm = RecordsManagerORM()
