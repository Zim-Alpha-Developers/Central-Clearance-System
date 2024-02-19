from dateutil.relativedelta import relativedelta
from django.shortcuts import redirect
from inertia import render
from marshmallow import ValidationError
from api.serializers import *
from django.http import JsonResponse
import json
from django.core import serializers
from api.helper import *
from django.db.models import Q
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

def users_home(request):
    print("users Home")
    return render(request, "User/Dashboard", props={})
