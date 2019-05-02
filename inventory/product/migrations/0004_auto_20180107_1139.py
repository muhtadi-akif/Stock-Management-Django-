# Generated by Django 2.0.1 on 2018-01-07 11:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20180107_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cone_quantity_value',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='notifications',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 1, 7, 11, 38, 59, 9593)),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 1, 7, 11, 38, 59, 4377)),
        ),
        migrations.AlterField(
            model_name='team',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 1, 7, 11, 38, 59, 5893)),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 1, 7, 11, 38, 59, 8081)),
        ),
    ]
