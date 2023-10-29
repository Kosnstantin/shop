from django.shortcuts import render
from categories.models import Goods, SubCategory, Laptop, PC, PetFood
# from categories.views import 
# Create your views here.


def good_page(request, good_pk):
    good = Goods.objects.get(pk=good_pk)
    context = {"good": good}
    return render(request, "goods/goods.html", context)
