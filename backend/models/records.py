from sqlalchemy import func
from backend.models.db import db


class RecordModel(db.Model):
    __tablename__ = "records"

    record_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.String(256), db.ForeignKey("users.user_id"), unique=False, nullable=False
    )
    category_id = db.Column(
        db.Integer, db.ForeignKey("categories.category_id"), unique=False, nullable=False
    )
    record_date = db.Column(db.TIMESTAMP, server_default=func.now())
    record_sum = db.Column(db.Float(precision=2), unique=False, nullable=False)

    user = db.relationship("UserModel", back_populates="records")
    category = db.relationship("CategoryModel", back_populates="records")
