from django.http import JsonResponse
from django.shortcuts import render
from categories.models import Goods, SubCategory, Laptop, PC, PetFood
from django.template.loader import render_to_string

# Create your views here.


def good_page(request, good_pk):
    good = Goods.objects.get(pk=good_pk)
    context = {"good": good}
    return render(request, "goods/goods.html", context)


def good_info(request, good_pk):
    good = Goods.objects.get(pk=good_pk)
    filtered_data = render_to_string("goods/good_info.html", {"good": good})
    return JsonResponse({"data": filtered_data})


def characteristics(request, good_pk):
    good = Goods.objects.get(pk=good_pk)
    filtered_data = render_to_string("goods/good_characteristic.html", {"good": good})
    return JsonResponse({"data": filtered_data})


def add_review(request, good_pk):
    good = Goods.objects.get(pk=good_pk)
    filtered_data = render_to_string("goods/add_review.html", {"good": good})
    return JsonResponse({"data": filtered_data})
