from django.db import models


# модель категорий
class Category(models.Model):
    text = models.CharField(max_length=100, verbose_name="Add category")

    def __str__(self):
        return f"{self.text}"


class Goods(models.Model):
    # подключение к модели категорий с помощью внешнего ключа
    subcategory = models.ForeignKey(
        "SubCategory", on_delete=models.CASCADE, blank=True, null=True
    )
    title = models.CharField(max_length=100, verbose_name="Title")
    price = models.IntegerField(verbose_name="Price")
    characteristics = models.TextField(verbose_name="Characteristics")

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.title}"


class Laptop(Goods):
    processor_type = models.CharField(max_length=50, verbose_name="Processor Type")
    screen_size = models.DecimalField(
        max_digits=4, decimal_places=2, verbose_name="Screen Size"
    )


class Monitor(Goods):
    screen_size = models.DecimalField(
        max_digits=4, decimal_places=2, verbose_name="Screen Size"
    )
    refresh_rate = models.IntegerField(verbose_name="Refresh Rate")


class PetFood(Goods):
    pet_type = models.CharField(max_length=50, verbose_name="Pet Type")


class SubCategory(models.Model):
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, blank=True, null=True
    )
    title = models.CharField(max_length=100, verbose_name="Title")

    def __str__(self):
        return f"{self.title}"
