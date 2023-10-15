from django.shortcuts import render
from categories.models import Category, SubCategory

# Create your views here.


def home(request):
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    context = {"categories": categories, "subcategories": subcategories}
    return render(request, "shop/home.html", context)
