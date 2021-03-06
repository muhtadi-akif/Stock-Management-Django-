# Generated by Django 2.0.1 on 2018-01-07 11:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20180107_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='changeValue',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 1, 7, 11, 8, 34, 436208)),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 1, 7, 11, 8, 34, 433037)),
        ),
        migrations.AlterField(
            model_name='team',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 1, 7, 11, 8, 34, 433900)),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 1, 7, 11, 8, 34, 435324)),
        ),
    ]
