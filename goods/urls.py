from django.contrib import admin
from django.urls import path
from goods.views import good_page

urlpatterns = [
    path("good/<int:good_pk>", good_page, name="good_page"),
]
