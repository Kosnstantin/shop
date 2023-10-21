from django.contrib import admin
from categories.models import Goods, Category, SubCategory, Laptop, PC, PetFood

# Register your models here.

admin.site.register(Laptop)
admin.site.register(PC)
admin.site.register(PetFood)
admin.site.register(Category)
admin.site.register(SubCategory)
