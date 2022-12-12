from backend.data.db.models.db import db


class CurrencyModel(db.Model):
    __tablename__ = "currencies"

    currency_id = db.Column(db.Integer, primary_key=True)
    currency_name = db.Column(db.String(256), unique=True, nullable=False)

    users = db.relationship(
        "UserModel", back_populates="currencies", lazy="dynamic"
    )
