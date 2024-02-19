from apps.authentication.models import *
from django.conf import settings
import requests as request
from apps.api.models import *


def get_user(request):
    user = request.user
    return user