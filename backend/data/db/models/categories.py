from backend.data.db.models.db import db


class CategoryModel(db.Model):
    __tablename__ = "categories"

    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(256), unique=True, nullable=False)

    record_category = db.relationship(
        "RecordModel", back_populates="category", foreign_keys="RecordModel.category_id", lazy="dynamic"
    )
