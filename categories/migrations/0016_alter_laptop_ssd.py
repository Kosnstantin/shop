# Generated by Django 4.2.5 on 2023-10-16 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0015_alter_laptop_ssd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='ssd',
            field=models.IntegerField(default=200, max_length=50, null=True, verbose_name='Operating System'),
        ),
    ]
