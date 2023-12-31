# Generated by Django 4.2.5 on 2023-10-15 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_tra_remove_goods_category_goods_tra'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='categories.category')),
            ],
        ),
        migrations.RemoveField(
            model_name='goods',
            name='Tra',
        ),
        migrations.DeleteModel(
            name='Tra',
        ),
        migrations.AddField(
            model_name='goods',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='categories.subcategory'),
        ),
    ]
