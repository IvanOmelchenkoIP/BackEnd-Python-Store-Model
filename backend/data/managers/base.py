from abc import ABC, abstractmethod


class LoginManager(ABC):
    @abstractmethod
    def register(self, user_data):
        pass

    @abstractmethod
    def login(self, user_data):
        pass


class UsersManager(ABC):
    @abstractmethod
    def get_users(self):
        pass

    @abstractmethod
    def get_user_by_id(self, user_id):
        pass

    @abstractmethod
    def set_user_currency(self, user_data, user_id):
        pass


class CurrenciesManager(ABC):
    @abstractmethod
    def add(self, currency_data):
        pass

    @abstractmethod
    def get_currencies(self):
        pass

    @abstractmethod
    def get_currency_by_id(self, currency_id):
        pass


class CategoriesManager(ABC):
    @abstractmethod
    def add(self, category_data):
        pass

    @abstractmethod
    def get_categories(self):
        pass

    @abstractmethod
    def get_category_by_id(self, category_id):
        pass

class RecordsManager(ABC):
    @abstractmethod
    def add(self, record_data):
        pass

    @abstractmethod
    def get_records_by_user_categories(self, kwargs):
        pass

    @abstractmethod
    def get_record_by_id(self, record_id):
        pass