from django.contrib import admin
from categories.models import Goods, Category, SubCategory, Laptop

# Register your models here.

admin.site.register(Laptop)
admin.site.register(Category)
admin.site.register(SubCategory)
