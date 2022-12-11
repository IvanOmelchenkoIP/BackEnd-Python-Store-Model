from flask import jsonify
from flask_smorest import abort

from backend.data.managers.base import RecordsManager

from backend.data.db.storages.db import categories, users, records, currencies
from backend.utils.utils import contains


class RecordsManagerStorage(RecordsManager):
    def add(self, record_data):
        if not contains(users.get_users(), "user_id", record_data["user_id"]):
            abort(404, message="Can only add record for existing user_id!")
        if not contains(categories.get_categories(), "category_id", record_data["category_id"]):
            abort(404, message="Can only add record for existing category_id!")
        if "record_currency" in record_data:
            if not contains(currencies.get_currencies(), "currency_id", record_data["record_currency"]):
                abort(404, message="Can only add record for existing currency!")
        return jsonify(records.add(record_data, users.get_users()))

    def get_records_by_user_categories(self, kwargs):
        return jsonify(records.get_records_by_user_categories(kwargs.get("user_id"), kwargs.get("category_id")))

    def get_record_by_id(self, record_id):
        selected = records.get_record_by_id(record_id)
        if not selected:
            abort(404, message="Record does not exist!")
        return jsonify(selected[0])
