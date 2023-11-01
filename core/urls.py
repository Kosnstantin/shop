from django.contrib import admin
from django.urls import path, include
# from core.views import SnippetData


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("shop.urls")),
    path("", include("authentic.urls")),
    path("", include("categories.urls")),
    path("", include("goods.urls")),
    # path("api-auth/", include("rest_framework.urls")),
    # path("auth/", include("djoser.urls")),
    # path("auth/", include("djoser.urls.jwt")),
    # path("test/", SnippetData.as_view()),
]
