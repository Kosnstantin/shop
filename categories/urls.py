from django.contrib import admin
from django.urls import path
from categories.views import subcategory

urlpatterns = [
    path("subcategory/<int:subcategory_pk>", subcategory, name="subcategory")
]
