from django.urls import path, include
from goods.views import goods_list

urlpatterns = [path("goods", goods_list, name="goods_list")]
