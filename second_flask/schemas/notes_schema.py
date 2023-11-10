from marshmallow import Schema, fields, validate


class NotesSchema(Schema):

    title = fields.Str(
        required=True,
        default="Title",
        validate=[
            validate.Length(min=3, max=70)
        ]
    )

    desc = fields.Str(
        required=False
    )


# TODO -> # do user_id needed to be validated?
# Check how many field to be validated with this schema
# can we validate all with schema which added in model?

# WE CAN PASS `ONLY` AND `EXCLUDE` KEYWORD TO SCHEMA OR FIELDS TO VALIDATE.
# https://chat.openai.com/share/297b3742-34b3-4288-ae4a-689aa9ad0b04
