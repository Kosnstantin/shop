from django.shortcuts import render
from categories.models import Goods, SubCategory

# Create your views here.


def subcategory(request, subcategory_pk):
    subcategory = SubCategory.objects.get(pk=subcategory_pk)
    goods = Goods.objects.filter(subcategory=subcategory)
    context = {"goods": goods, "subcategory": subcategory}
    return render(request, "categories/subcategories.html", context)
