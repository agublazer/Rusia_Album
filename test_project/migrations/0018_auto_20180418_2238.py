# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-19 03:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_project', '0017_auto_20180418_2222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cromo_rep',
            name='id',
        ),
        migrations.AlterField(
            model_name='cromo_rep',
            name='no_repeat',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
