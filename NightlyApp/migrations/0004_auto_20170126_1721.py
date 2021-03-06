# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 17:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NightlyApp', '0003_day_sales'),
    ]

    operations = [
        migrations.RenameField(
            model_name='day',
            old_name='sales',
            new_name='LBW_sales',
        ),
        migrations.RenameField(
            model_name='day',
            old_name='closing_manager',
            new_name='managers',
        ),
        migrations.AddField(
            model_name='day',
            name='TCI_percentage',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='day',
            name='TCI_variance',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='day',
            name='WTD_budget',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='day',
            name='WTD_sales',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='day',
            name='WTD_sales_last_year',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='day',
            name='beer_sales',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='day',
            name='beverage_sales',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='day',
            name='boh_actual',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='day',
            name='boh_target',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='day',
            name='boh_variance',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='day',
            name='comp_11',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='day',
            name='comp_2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='day',
            name='comp_4',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='day',
            name='comp_6',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='day',
            name='comp_7',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='day',
            name='comp_8',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='day',
            name='deliveries_sales',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='day',
            name='drop_variance',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='day',
            name='foh_actual',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='day',
            name='foh_target',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='day',
            name='foh_variance',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='day',
            name='food_harvest',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='day',
            name='food_sales',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='day',
            name='forecast',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='day',
            name='last_year',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='day',
            name='liquor_mix',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='day',
            name='liquor_sales',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='day',
            name='lunch_sales',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='day',
            name='net_sales',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='day',
            name='pc_drawer',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='day',
            name='takeaway_percentage',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='day',
            name='takeaway_sales',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='day',
            name='vs_lastyear',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='day',
            name='week_vs_lastyear',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='day',
            name='wine_sales',
            field=models.IntegerField(default=0),
        ),
    ]
