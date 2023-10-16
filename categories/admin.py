from django.contrib import admin
from categories.models import Category, SubCategory, Laptop

# Register your models here.

# admin.site.register(Goods)
admin.site.register(Laptop)

admin.site.register(Category)
admin.site.register(SubCategory)
