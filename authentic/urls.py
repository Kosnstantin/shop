from django.urls import path, include
from authentic.views import UserRegistrationView
from authentic.views import registration_view, reg
urlpatterns = [
    path("registration/", registration_view, name="registration"),
    path("registration/submit/", UserRegistrationView.as_view(), name="user-registration-submit"),
    path("correctregisrt/", reg, name="correctregisrt")
]
