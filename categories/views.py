from django.shortcuts import render
from categories.models import Category

# Create your views here.


def cat_list(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "shop/home.html", context)


