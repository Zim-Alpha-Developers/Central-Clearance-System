
# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from inertia import inertia, render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods
from . import serializers, EmailBackEnd
from marshmallow import ValidationError
from inertia.share import share
from authentication.models import *
from api.helper import *
from api.views import *

def login_view(request):
    if request.method == "POST":
        login_schema = serializers.LoginSchema()
        try:
            data = login_schema.loads(request.body)
        except ValidationError as err:
            props = {
                "error": {
                    "type": "error",
                    "message": "Something went wrong!",
                }
            }
            return render(request, "Auth/Login", props)
        else:
            user = EmailBackEnd.authenticate(
                request, username=data.get("email"), password=data.get("password")
            )

            if user != None:
                login(request, user)
                return redirect("home")
            else:
                props = {
                    "error": {"type": "error", "message": "Invalid login credentials"}
                }
                return render(request, "Auth/Login", props)
    else:
        props = {}
        return render(request, "Auth/Login", props)

def forgot_password(request):
    pass
    return render(request, "Auth/Login", props={})

@require_http_methods(["GET"])
def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")
