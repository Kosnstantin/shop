from django.http import JsonResponse
from django.shortcuts import render
from categories.models import Goods, SubCategory, Laptop, PC, PetFood
from django.template.loader import render_to_string
from django.db.models import Q
from django.apps import apps

# Create your views here.


def fil(goods_filtername, goods):
    goods_fields_verbovse_name = {}
    for field in goods_filtername:
        verbose_name = field.verbose_name

        if (
            verbose_name != "ID"
            and verbose_name != "subcategory"
            and verbose_name != "Characteristics"
            and verbose_name != "goods ptr"
        ):
            field_value = set([getattr(obj, field.name) for obj in goods])
            field_list = list(field_value)
            field_dict = {verbose_name: field_list}

            goods_fields_verbovse_name[field.name] = field_dict
            # goods_fields_verbovse_name[field.name] = field_value
    print(goods_fields_verbovse_name)
    return goods_fields_verbovse_name


subcategory_to_product_model = {
    "PC": PC,
    "Laptop": Laptop,
    "PetFood": PetFood,
}


def subcategory(request, subcategory_pk):
    subcategory = SubCategory.objects.get(pk=subcategory_pk)

    for name_model in subcategory_to_product_model:
        if name_model == subcategory.title:
            nm = name_model

    model_class_for_filter = apps.get_model("categories", nm)
    goods = model_class_for_filter.objects.filter(subcategory=subcategory)

    fields_of_select_model = model_class_for_filter._meta.get_fields()

    fields_verbovse_name = fil(fields_of_select_model, goods)

    context = {
        "goods": goods,
        "subcategory": subcategory,
        "fields_verbovse_name": fields_verbovse_name,
        "fields_of_select_model": fields_of_select_model,
    }
    return render(request, "categories/subcategories.html", context)


def filter_data(request, subcategory_pk):
    subcategory = SubCategory.objects.get(pk=subcategory_pk)
    for name_model in subcategory_to_product_model:
        if name_model == subcategory.title:
            nm = name_model

    model_class_for_filter = apps.get_model("categories", nm)
    allGoods = (
        model_class_for_filter.objects.filter(subcategory=subcategory)
        .order_by("-id")
        .distinct()
    )
    if model_class_for_filter is None:
        # Обработка ошибки, если не найдена подходящая модель
        return JsonResponse({"error": "Model not found"})
    q_objects = Q()

    for field_name in model_class_for_filter._meta.get_fields():
        field_name = field_name.name
        field_values = request.GET.getlist(field_name + "[]")

        if field_values:
            q_objects |= Q(**{f"{field_name}__in": field_values})

    if q_objects:
        allGoods = allGoods.filter(q_objects).distinct()

    filtered_data = render_to_string(
        "categories/subcategories.html", {"goods": allGoods}
    )

    return JsonResponse({"data": filtered_data})
