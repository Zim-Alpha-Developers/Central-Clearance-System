# Create your views here.
from django.http import HttpResponse
from inertia import inertia, render
from django.shortcuts import redirect
from django.http import JsonResponse


def index(request):
    user = request.user
    # Check whether the user is logged in or not
    if user.is_authenticated:
        if user.user_type == 1:
            pass
        elif user.user_type == 2:
            pass
        else:
            return redirect("login")
    else:
        return redirect("login")
