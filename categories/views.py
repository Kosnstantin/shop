from django.http import JsonResponse
from django.shortcuts import render
from categories.models import Goods, SubCategory, Laptop, PC, PetFood
from django.views.generic import ListView
from django.template.loader import render_to_string
from django.db.models import Q
from django.apps import apps
# Create your views here.


def fil(goods_filtername, modelName):
    goods_fields_verbovse_name = []
    for i in goods_filtername:
        if (
            i.verbose_name != "ID"
            and i.verbose_name != "subcategory"
            and i.verbose_name != "Characteristics"
        ):
            field = i.verbose_name
            goods_fields_verbovse_name.append(field)
    return goods_fields_verbovse_name


subcategory_to_product_model = {
    "PC": PC,
    "Laptop": Laptop,
    "PetFood": PetFood,
    # Добавьте остальные подкатегории и модели продуктов
}
# subcategory_to_product_model = [PC, Laptop]

# for i in 
def subcategory(request, subcategory_pk):
    subcategory = SubCategory.objects.get(pk=subcategory_pk)
    goods = Goods.objects.filter(subcategory=subcategory)

    for name_cat in subcategory_to_product_model:
        if name_cat == subcategory.title:
            nm = name_cat
  
    sn = apps.get_model('categories', nm)
    fields = sn._meta.get_fields()
    fields_verbovse_name = fil(fields, sn)

    # laptops_fields = Laptop._meta.get_fields()
    # laptops_fields_verbovse_name = fil(laptops_fields, Laptop)
    # monitor_fileds = Monitor._meta.get_fields()
    # product_model = subcategory_to_product_model.get(subcategory_name, None)
    # print(i)
    # print(product_model)
    context = {
        "goods": goods,
        "subcategory": subcategory,
        "fields_verbovse_name": fields_verbovse_name
        # "laptops_fileds_verbovse_name": laptops_fields_verbovse_name,
        # "monitor_fileds": monitor_fileds,
    }
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
