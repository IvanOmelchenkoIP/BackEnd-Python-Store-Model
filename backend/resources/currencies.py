from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import IntegrityError

from backend.models.db import db
from backend.models.currencies import CurrencyModel

from backend.resources.schemas import CurrencySchema


blp = Blueprint(
    "currency", __name__, description="Blueprint for operations on currencies"
)


@blp.route("/currency/<string:currency_id>")
class Currency(MethodView):
    @blp.response(200, CurrencyModel)
    def get(self, currency_id):
        return CurrencyModel.query.get_or_404(currency_id)


@blp.route("/currency")
class Currency(MethodView):
    @blp.arguments(CurrencySchema)
    @blp.response(200, CurrencySchema)
    def post(self, category_data):
        # if contains(categories.get_categories(), "category_name", category_data["category_name"]):
        #    abort(404, message="The category already exists!")
        # return jsonify(categories.add(category_data))
        currency = CurrencyModel(**category_data)
        try:
            db.session.add(currency)
            db.session.commit()
        except IntegrityError:
            abort(404, message="The category already exists!")
        return currency

    @blp.response(200, CurrencySchema(many=True))
    def get(self):
        # return jsonify(categories.get_categories())
        return CurrencyModel.query.all()
