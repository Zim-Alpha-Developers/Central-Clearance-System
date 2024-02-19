from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as ValidError
from marshmallow import Schema, ValidationError, fields

# from . import utils


def password_validation(value):
    try:
        validate_password(value)
    except ValidError as error:
        raise ValidationError(error)


class RegisterSchema(Schema):
    firstName = fields.Str(required=True)
    lastName = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=password_validation)


class LoginSchema(Schema):
    email = fields.Str(required=True)
    password = fields.Str(required=True)
