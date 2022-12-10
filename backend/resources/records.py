from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint

from backend.schemas.schemas import RecordSchema, RecordRequestSchema

from backend.managers.storages.managers import records_storage
from backend.managers.models.managers import records_orm

blp = Blueprint(
    "record", __name__, description="Blueprint for operations on records"
)


@blp.route("/record/<string:record_id>")
@jwt_required()
class Record(MethodView):
    @blp.response(200, RecordSchema)
    def get(self, record_id):
        #record = records_storage.get_records_by_id(record_id)
        record = records_orm.get_records_by_id(record_id)
        return record


@blp.route("/record")
@jwt_required()
class Records(MethodView):
    @blp.arguments(RecordSchema)
    @blp.response(200, RecordSchema)
    def post(self, record_data):
        #record = records_storage.add(record_data)
        record = records_orm.add(record_data)
        return record

    @blp.arguments(RecordRequestSchema, location="query", as_kwargs=True)
    @blp.response(200, RecordSchema(many=True))
    def get(self, **kwargs):
        #records = records_storage.get_records_by_user_categories(kwargs)
        records = records_orm.get_records_by_user_categories(kwargs)
        return records
