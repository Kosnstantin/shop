from django.contrib import admin
from categories.models import Goods, Category, SubCategory

# Register your models here.

admin.site.register(Goods)
admin.site.register(Category)
admin.site.register(SubCategory)

