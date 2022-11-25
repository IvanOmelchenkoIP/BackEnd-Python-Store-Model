from sqlalchemy import func, text
from backend.models.db import db


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
        db.Integer, db.ForeignKey("users.user_currency"), unique=False
    )
    currency = db.relationship(
        "UserModel", back_populates="record_currency", foreign_keys=record_currency
    )

    #users = db.relationship("UserModel", back_populates="records")
    #categories = db.relationship("CategoryModel", back_populates="records")

    #user = db.relationship("UserModel", back_populates="records", foreign_keys=[user_id])
    #currency = db.relationship("UserModel", back_populates="records", foreign_keys=[record_currency])
