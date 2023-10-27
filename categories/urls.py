from django.contrib import admin
from django.urls import path
from categories.views import filter_data, subcategory

urlpatterns = [
    path("subcategory/<int:subcategory_pk>", subcategory, name="subcategory"),
    path("filter-data/<int:subcategory_pk>", filter_data, name="filter_data"),
]
