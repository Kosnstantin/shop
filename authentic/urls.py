from django.urls import path, include
from authentic.views import UserRegistrationView, registr, successfulreg

urlpatterns = [
    path("registr", registr, name="registr"),
    path("registr/submit", UserRegistrationView.as_view(), name="user-registration"),
    path("registr/successfulreg", successfulreg, name="successfulreg"),
]
