# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 01:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NightlyApp', '0002_day_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='day',
            name='sales',
            field=models.IntegerField(default=0),
        ),
    ]
