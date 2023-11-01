from django.urls import path
from authentic.views import (
    UserLoginView,
    UserRegistrationView,
    registr,
    successfulreg,
    log,
)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("registr/", registr, name="registr"),
    path("registr/submit", UserRegistrationView.as_view(), name="user-registration"),
    path("registr/successfulreg", successfulreg, name="successfulreg"),
    path("autorize/", log, name="autorize"),
    path("autorize/submit", UserLoginView.as_view(), name="user-autorize"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
