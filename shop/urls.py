from django.urls import path, include
from shop.views import home

urlpatterns = [path("", home, name="home")]
