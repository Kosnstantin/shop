# Generated by Django 4.2.5 on 2023-10-16 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0007_remove_goods_characteristics'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='characteristics',
            field=models.TextField(null=True, verbose_name='Characteristics'),
        ),
    ]