# Generated by Django 4.2.5 on 2023-10-16 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0017_remove_laptop_ssd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laptop',
            name='brand',
        ),
    ]