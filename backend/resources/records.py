from flask import jsonify

from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import IntegrityError

from backend.models.db import db
from backend.models.records import RecordModel

from backend.schemas.schemas import RecordSchema, RecordRequestSchema

from sqlalchemy import text

from backend.storages.db import categories, users, records
from backend.utils.utils import contains

blp = Blueprint(
    "record", __name__, description="Blueprint for operations on records"
)


@blp.route("/record/<string:record_id>")
class Record(MethodView):
    @blp.response(200, RecordSchema)
    def get(self, record_id):
        #selected = records.get_record_by_id(record_id)
        # if not selected:
        #    abort(404, message="Record does not exist!")
        # return jsonify(selected[0])
        return RecordModel.query.get_or_404(record_id)


@blp.route("/record")
class Records(MethodView):
    @blp.arguments(RecordSchema)
    @blp.response(200, RecordSchema)
    def post(self, record_data):
        # if not contains(users.get_users(), "user_id", record_data["user_id"]):
        #    abort(404, message="Can only add record for existing user_id!")
        # if not contains(categories.get_categories(), "category_id", record_data["category_id"]):
        #    abort(404, message="Can only add record for existing category_id!")
        # if "record_currency" in record_data:
        #    if not contains(users.get_users(), "user_currency", record_data["record_currency"]):
        #        abort(404, message="Can only add record for existing currency!")
        # return jsonify(records.add(record_data, users.get_users()))
        record = RecordModel(**record_data)
        try:
            db.session.add(record)
            db.session.commit()
        except IntegrityError:
            abort(400, message="There was an error creating a new record!")
        return record

    @blp.arguments(RecordRequestSchema, location="query", as_kwargs=True)
    @blp.response(200, RecordSchema(many=True))
    def get(self, **kwargs):
        # return jsonify(records.get_records(kwargs.get("user_id"), kwargs.get("category_id")))
        user_id = kwargs.get("user_id")
        category_id = kwargs.get("category_id")
        if (user_id == None):
            return RecordModel.query.all()
        query = RecordModel.query.filter_by(user_id=user_id)
        if category_id:
            query = query.filter_by(category_id=category_id)
        return query.all()
