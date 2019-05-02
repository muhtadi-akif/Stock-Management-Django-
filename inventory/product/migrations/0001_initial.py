# Generated by Django 2.0.1 on 2018-01-07 08:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('used', models.IntegerField(default=0)),
                ('changeValue', models.IntegerField()),
                ('valueProgress', models.IntegerField()),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime(2018, 1, 7, 8, 5, 37, 624963))),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('unit_name', models.CharField(max_length=100)),
                ('per_unit_price', models.FloatField()),
                ('total_unit_price', models.FloatField()),
                ('team_name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime(2018, 1, 7, 8, 5, 37, 619497))),
                ('quantity_value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime(2018, 1, 7, 8, 5, 37, 621126))),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_member_name', models.CharField(max_length=100)),
                ('team_member_position', models.CharField(max_length=100)),
                ('team_member_username', models.CharField(max_length=100)),
                ('team_member_password', models.CharField(max_length=50)),
                ('team', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime(2018, 1, 7, 8, 5, 37, 623992))),
            ],
        ),
        migrations.CreateModel(
            name='Units',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name', models.CharField(max_length=50)),
                ('unit_si_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='notifications',
            name='changedID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product'),
        ),
        migrations.AddField(
            model_name='notifications',
            name='changerID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.TeamMember'),
        ),
    ]