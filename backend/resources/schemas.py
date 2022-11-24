from marshmallow import Schema, fields


class UserSchema(Schema):
    user_id = fields.Str(dump_only=True)
    user_name = fields.Str(required=True)


class CategorySchema(Schema):
    category_id = fields.Str(dump_default=True)
    category_name = fields.Str(required=True)


class RecordSchema(Schema):
    record_id = fields.Str(dump_default=True)
    user_id = fields.Str(required=True)
    category_id = fields.Str(required=True)
    record_sum = fields.Float(required=True)
    record_date = fields.DateTime(dump_default=True)
