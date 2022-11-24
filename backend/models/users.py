from backend.models.db import db


class UserModel(db.Model):
    __tablname__ = "user"

    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(256), unique=True, nullable=False)
