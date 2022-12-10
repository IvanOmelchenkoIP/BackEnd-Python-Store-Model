from marshmallow import Schema, fields


class UserSchema(Schema):
    user_id = fields.Int(dump_only=True)
    user_name = fields.Str(required=True)
    user_currency = fields.Int(required=True)
    user_passwd = fields.Str(required=True)


class UserLoginSchema(Schema):
    user_name = fields.Str(required=True)
    user_passwd = fields.Str(required=True)


class UserTokenSchema(Schema):
    user_id = fields.Int(required=True)
    access_token = fields.Str(required=True)


class UserCurrencySchema(Schema):
    user_currency = fields.Int(required=True)


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
    record_currency = fields.Int()


class CurrencySchema(Schema):
    currency_id = fields.Int(dump_default=True)
    currency_name = fields.String(required=True)
