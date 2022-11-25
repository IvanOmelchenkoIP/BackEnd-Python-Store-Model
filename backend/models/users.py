from backend.models.db import db


class UserModel(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(256), unique=True, nullable=False)
    user_currency = db.Column(
        db.Integer, db.ForeignKey("currencies.currency_id"), unique=False
    )

    currencies = db.relationship("CurrencyModel", back_populates="users")
    records = db.relationship(
        "RecordModel", back_populates="users", lazy="dynamic"
    )
