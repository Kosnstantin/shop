# Generated by Django 4.2.5 on 2023-10-16 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0008_goods_characteristics'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptop',
            name='brand',
            field=models.CharField(default='None brand', max_length=50, verbose_name='Brand'),
        ),
        migrations.AddField(
            model_name='laptop',
            name='num_proc_cores',
            field=models.IntegerField(default=3, verbose_name='Number of processor cores'),
        ),
        migrations.AddField(
            model_name='laptop',
            name='operating_memory',
            field=models.IntegerField(default=4, verbose_name='RAM (GB)'),
        ),
        migrations.AddField(
            model_name='laptop',
            name='operating_system',
            field=models.CharField(default='None info', max_length=50, verbose_name='Operating System'),
        ),
        migrations.AddField(
            model_name='laptop',
            name='ssd',
            field=models.IntegerField(default='None info', verbose_name='SSD (GB)'),
        ),
        migrations.AddField(
            model_name='laptop',
            name='video_card',
            field=models.CharField(default='None info', max_length=50, verbose_name='Video card'),
        ),
        migrations.AddField(
            model_name='laptop',
            name='video_card_memory_capacity',
            field=models.IntegerField(default='None info', verbose_name='Video card memory capacity (GB)'),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='processor_type',
            field=models.CharField(default='None info', max_length=50, verbose_name='Processor Type'),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='screen_size',
            field=models.DecimalField(decimal_places=2, default='None info', max_digits=4, verbose_name='Screen Size'),
        ),
    ]
