from django.contrib import admin
from django.urls import path
from goods.views import good_page, good_info, characteristics, add_review

urlpatterns = [
    path("good/<int:good_pk>", good_page, name="good_page"),
    path("good_info/<int:good_pk>/", good_info, name="good_info"),
    path("characteristics/<int:good_pk>/", characteristics, name="characteristics"),
    path("add_review/<int:good_pk>/", add_review, name="add_review"),
]
