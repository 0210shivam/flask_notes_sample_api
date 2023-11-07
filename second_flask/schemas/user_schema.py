from marshmallow import Schema, fields, validate


class UserSchema(Schema):

    username = fields.Str(
        required=True,
        validate=[
            validate.Length(min=3),
            validate.Regexp(r'^[a-zA-Z0-9_]*$', error="Username must contain only letters, numbers, and underscores"),
            validate.Length(max=20, error="Username must be no more than 20 characters long")
        ]
    )

    email = fields.Email(
        required=True,
        validate=[
            validate.Email(),
            validate.Length(max=100),
            validate.Regexp(r'^[^@]+@[^@]+\.[^@]+$', error="Invalid email format"),  # Custom regex validation
        ]
    )

    password = fields.Str(
        required=True,
        validate=[
            validate.Length(min=6, error="Password should be more than six characters.")
        ]
    )
