# users/urls.py

from users.views import dashboard, register
from django.urls import path, include

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("oauth/", include("social_django.urls")),
    path("register/", register, name="register"),
]