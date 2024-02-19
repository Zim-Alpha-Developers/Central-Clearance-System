"""
Serializers for the api app.
"""
from marshmallow import Schema, fields, validate, ValidationError
from datetime import datetime
from rest_framework import serializers
from django.utils import timezone
from api.models import *
from authentication.models import CustomUser
from django.db.models import Q
from authentication.serializers import *
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate as django_authenticate
import re


# from . import models

class CreateAccountSchema(Schema):
    """
    A schema definition using the Marshmallow library in Python.
    Used for validating and serializing data related to a search operation.
    """

    username = fields.Str(
        data_key="username",
        required=True,
    )
    password = fields.Str(
        data_key="password", required=True, validate=validate.Length(min=6)
    )
    confirmPassword = fields.Str(data_key="confirmPassword")


# from . import models
class SearchSchema(Schema):
    """
    A schema definition using the Marshmallow library in Python.
    Used for validating and serializing data related to a search operation.
    """

    searchParam = fields.Str(
        data_key="searchParam", required=True, validate=validate.Length(min=3)
    )
    """
    A string field that represents the search parameter. 
    It is required and must have a minimum length of 3 characters.
    """

    searchValue = fields.Str(
        data_key="searchValue", required=True, validate=validate.Length(min=1)
    )
    """
    A string field that represents the search value. 
    It is required and must have a minimum length of 1 character.
    """


class FileSerializer(Schema):
    """
    A schema for serializing and deserializing file data.

    Fields:
    - file: A field of type Raw that represents the file data. It is marked as dump_only=True, meaning it is only used for serialization and not for deserialization.
    """

    file = fields.Raw(dump_only=True)

class UserSchema(Schema):
    """
    A schema definition using the Marshmallow library in Python.

    This class defines the structure and validation rules for individual data.
    """

    id = fields.Str(required=True)
    firstname = fields.Str(required=True)
    surname = fields.Str(required=True)
    identification_number = fields.Str(required=True)

    def __init__(self, *args, **kwargs):
        """
        Initialize the IndividualSchema class.

        Parameters:
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)



