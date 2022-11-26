from flask_smorest import abort
from sqlalchemy.exc import IntegrityError

from backend.models.db import db
from backend.models.records import RecordModel


class RecordsManagerORM:
    def add(self, record_data):
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

    def get_records_by_id(self, record_id):
        return RecordModel.query.get_or_404(record_id)
