from django.contrib import admin
from django.urls import path
from categories.views import cat_list


urlpatterns = [path("catlist", cat_list, name="cat_list")]
