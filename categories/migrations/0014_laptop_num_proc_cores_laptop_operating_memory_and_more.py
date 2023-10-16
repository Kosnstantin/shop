# Generated by Django 4.2.5 on 2023-10-16 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0013_remove_laptop_num_proc_cores_and_more'),
    ]

    operations = [
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
            name='screen_size',
            field=models.DecimalField(decimal_places=2, default=13, max_digits=4, verbose_name='Screen Size (″)'),
        ),
        migrations.AddField(
            model_name='laptop',
            name='ssd',
            field=models.CharField(default='None info', max_length=50, verbose_name='Operating System'),
        ),
        migrations.AddField(
            model_name='laptop',
            name='video_card',
            field=models.CharField(default='None info', max_length=50, verbose_name='Video card'),
        ),
        migrations.AddField(
            model_name='laptop',
            name='video_card_memory_capacity',
            field=models.IntegerField(default=1, verbose_name='Video card memory capacity (GB)'),
        ),
    ]
