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
    text = models.TextField(verbose_name="Text")
    price = models.IntegerField(verbose_name="Price")
    characteristics = models.TextField(verbose_name="Characteristics")


    def __str__(self):
        return f"{self.title}"


class SubCategory(models.Model):
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, blank=True, null=True
    )
    title = models.CharField(max_length=100, verbose_name="Title")

    def __str__(self):
        return f"{self.title}"
