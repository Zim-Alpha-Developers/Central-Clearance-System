from django.urls import path
from . import views

path("login/", views.login_view, name="login"),
path("logout_user/", views.logout_user, name="logout"),