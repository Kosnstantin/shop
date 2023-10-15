from django.shortcuts import render
from categories.models import Goods

# Create your views here.


def goods_list(request):
    goods = Goods.objects.all()
    context = {"goods": goods}
    return render(request, "goods/goods.html", context)
