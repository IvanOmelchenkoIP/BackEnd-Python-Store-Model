from backend.models.db import db


class CategoryModel(db.Model):
    __tablename__ = "categories"

    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(256), unique=True, nullable=False)

    record = db.relationship(
        "RecordModel", back_populates="categories", lazy="dynamic"
    )
