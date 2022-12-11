from flask_smorest import abort
from sqlalchemy.exc import IntegrityError

from backend.data.managers.base import RecordsManager

from backend.data.db.models.db import db
from backend.data.db.models.records import RecordModel
from backend.data.db.models.users import UserModel
from backend.data.db.models.categories import CategoryModel
from backend.data.db.models.currencies import CurrencyModel


class RecordsManagerORM(RecordsManager):
    def add(self, record_data):
        if not db.session.scalar(
            UserModel.query.filter_by(
                user_id=record_data["user_id"]
            )
        ):
            abort(404, message="Can only add existing users to record!")
        if not db.session.scalar(
            CategoryModel.query.filter_by(
                category_id=record_data["category_id"]
            )
        ):
            abort(404, message="Can only add existing categories to record!")
        if "record_currency" in record_data:
            if not db.session.scalar(
                CurrencyModel.query.filter_by(
                    currency_id=record_data["record_currency"]
                )
            ):
                abort(404, message="Can only add existing currency to record!")
        record = RecordModel(**record_data)
        try:
            db.session.add(record)
            db.session.commit()
        except IntegrityError:
            abort(400, message="There was an error creating a new record!")
        return record

    def get_records_by_user_categories(self, kwargs):
        user_id = kwargs.get("user_id")
        category_id = kwargs.get("category_id")
        if (user_id == None):
            return RecordModel.query.all()
        query = RecordModel.query.filter_by(user_id=user_id)
        if category_id:
            query = query.filter_by(category_id=category_id)
        return query.all()

    def get_record_by_id(self, record_id):
        return RecordModel.query.get_or_404(record_id)
