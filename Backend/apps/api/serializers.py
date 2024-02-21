"""
Serializers for the api app.
"""
from rest_framework import serializers
from .models import *

# from . import models

class IndividualSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualDetails
        fields = ['first_name', 'last_name', 'email']

print("IndividualSerializer")
