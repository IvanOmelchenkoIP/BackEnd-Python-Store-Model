from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint

from backend.endpoints.schemas.schemas import RecordSchema, RecordRequestSchema

#from backend.data.managers.storages.managers import records_manager
from backend.data.managers.models.managers import records_manager

blp = Blueprint(
    "record", __name__, description="Blueprint for operations on records"
)


@blp.route("/record/<string:record_id>")
class Record(MethodView):
    @blp.response(200, RecordSchema)
    @jwt_required()
    def get(self, record_id):
        record = records_manager.get_record_by_id(record_id)
        return record


@blp.route("/record")
class Records(MethodView):
    @blp.arguments(RecordSchema)
    @blp.response(200, RecordSchema)
    @jwt_required()
    def post(self, record_data):
        record = records_manager.add(record_data)
        return record

    @blp.arguments(RecordRequestSchema, location="query", as_kwargs=True)
    @blp.response(200, RecordSchema(many=True))
    def get(self, **kwargs):
        records = records_manager.get_records_by_user_categories(kwargs)
        return records
