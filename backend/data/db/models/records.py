from sqlalchemy import func

from backend.data.db.models.db import db


def set_default_currency(context):
    user_id = context.get_current_parameters()["user_id"]
    default_currency = db.session.scalar(
        db.select(db.text("users.user_currency"))
          .select_from(db.text("users"))
          .where(db.text("users.user_id==" + str(user_id)))
    )
    return default_currency


class RecordModel(db.Model):
    __tablename__ = "records"

    record_id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer, db.ForeignKey("users.user_id"), unique=False, nullable=False
    )
    user = db.relationship(
        "UserModel", back_populates="record_user", foreign_keys=user_id
    )

    category_id = db.Column(
        db.Integer, db.ForeignKey("categories.category_id"), unique=False, nullable=False
    )
    category = db.relationship(
        "CategoryModel", back_populates="record_category", foreign_keys=category_id
    )

    record_date = db.Column(db.TIMESTAMP, server_default=func.now())
    record_sum = db.Column(db.Float(precision=2), unique=False, nullable=False)

    record_currency = db.Column(
        db.Integer, db.ForeignKey("users.user_currency"), unique=False, default=set_default_currency
    )
    currency = db.relationship(
        "UserModel", back_populates="record_currency", foreign_keys=record_currency
    )
