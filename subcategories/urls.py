from django.urls import path, include
from subcategories.views import subcategory

urlpatterns = [
    path("subcategory/<int:subcategory_pk>", subcategory, name="subcategory")
]
