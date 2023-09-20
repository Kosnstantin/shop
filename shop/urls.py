from django.urls import path, include
from shop.views import task

urlpatterns = [path("", task, name="task")]
