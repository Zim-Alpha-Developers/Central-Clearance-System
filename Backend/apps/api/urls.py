from django.urls import path, include
from . import views
from .endpoints import admins, users

urlpatterns = [
    path("", views.index, name="home"),
    # admins url
        path(
            "admins/",
            include(
                [
                    path("", admins.admin_home, name="admin_home"),
                ]
                ),
            ),
        path(
        "users/",
        include(
            [
                path("", users.users_home, name="users_home"),
            ]
            ),
        ),
]