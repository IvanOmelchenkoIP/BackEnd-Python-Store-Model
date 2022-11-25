from marshmallow import Schema, fields


class UserSchema(Schema):
    user_id = fields.Int(dump_only=True)
    user_name = fields.Str(required=True)
    user_currency = fields.Int()


class CategorySchema(Schema):
    category_id = fields.Int(dump_default=True)
    category_name = fields.Str(required=True)


class RecordRequestSchema(Schema):
    user_id = fields.Int()
    category_id = fields.Int()


class RecordSchema(Schema):
    record_id = fields.Int(dump_default=True)
    user_id = fields.Int(required=True)
    category_id = fields.Int(required=True)
    record_sum = fields.Float(required=True)
    record_date = fields.DateTime(dump_default=True)


class CurrencySchema(Schema):
    currency_id = fields.Int(dump_default=True)
    currency_name = fields.String(required=True)
