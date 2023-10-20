from django.http import JsonResponse
from django.shortcuts import render
from categories.models import Goods, SubCategory, Laptop
from django.views.generic import ListView
from django.template.loader import render_to_string
from django.db.models import Q

# Create your views here.


def subcategory(request, subcategory_pk):
    subcategory = SubCategory.objects.get(pk=subcategory_pk)
    goods = Goods.objects.filter(subcategory=subcategory)
    laptops = Laptop.objects.all()
    # titles = Laptop.objects.filter().values('title__id','title__title','title__title_code').distinct()
    context = {"goods": goods, "subcategory": subcategory, "laptops": laptops}
    return render(request, "categories/subcategories.html", context)


def filter_data(request):
    titles = request.GET.getlist("title[]")
    prices = request.GET.getlist("price[]")
    allGoods = Goods.objects.all().order_by("-id").distinct()

    q_objects = Q()

    if titles:
        q_objects |= Q(title__in=titles)

    if prices:
        q_objects |= Q(price__in=prices)

    if q_objects:
        allGoods = allGoods.filter(q_objects).distinct()

    filtered_data = render_to_string(
        "categories/subcategories.html", {"goods": allGoods}
    )

    return JsonResponse({"data": filtered_data})
