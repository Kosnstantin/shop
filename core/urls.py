from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("shop.urls")),
    path("", include("authentic.urls")),
    # path("", include("categories.urls")),
]
