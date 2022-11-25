#from flask import jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import IntegrityError

from backend.models.db import db
from backend.models.records import RecordModel

from backend.resources.schemas import RecordSchema, RecordRequestSchema

#from backend.storages.storages import categories, users, records
#from backend.utils.utils import contains

blp = Blueprint(
    "record", __name__, description="Blueprint for operations on records"
)

@blp.route("/record/<string:record_id>")
class Record(MethodView):
    @blp.response(200, RecordSchema)
    def get(self, record_id):
        record = RecordModel.query.get_or_404(record_id)
        print(record.users.user_currency)
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
        # return jsonify(records.add(record_data))
        record = RecordModel(**record_data)
        try:
            db.session.add(record)
            db.session.commit()
        except IntegrityError:
            abort(
                404, message="Can only add record for existing user_id and category_id!"
            )
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
