# Generated by Django 2.0.1 on 2018-02-14 22:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20180214_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductEntryInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chequeNo', models.CharField(max_length=100)),
                ('supplier_name', models.CharField(max_length=100)),
                ('due_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('paid_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime(2018, 2, 14, 22, 48, 33, 499441))),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='cone_quantity_used_value',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='product_code',
            field=models.CharField(default='N/A', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='quantity_used_value',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 2, 14, 22, 48, 33, 505341)),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 2, 14, 22, 48, 33, 497845)),
        ),
        migrations.AlterField(
            model_name='suppliers',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 2, 14, 22, 48, 33, 507058)),
        ),
        migrations.AlterField(
            model_name='team',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 2, 14, 22, 48, 33, 500911)),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 2, 14, 22, 48, 33, 503548)),
        ),
        migrations.AddField(
            model_name='productentryinfo',
            name='productID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product'),
        ),
    ]
