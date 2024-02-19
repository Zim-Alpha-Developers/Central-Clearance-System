from dateutil.relativedelta import relativedelta
from django.shortcuts import redirect
from inertia import render
from marshmallow import ValidationError
from api.models import *
from api.serializers import *
from django.http import JsonResponse
import json
from django.core import serializers
from api.helper import *
from django.db.models import Q
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

def admin_home(request):
    print("Admins Home")
    return render(request, "Admin/Dashboard", props={})
