# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-24 21:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('test_project', '0019_auto_20180624_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='time_sobres',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 24, 21, 30, 9, 986110, tzinfo=utc)),
        ),
    ]
