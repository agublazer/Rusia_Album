# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-19 02:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_project', '0013_auto_20180418_2110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cromo_rep',
            name='cromo',
        ),
        migrations.AddField(
            model_name='cromo',
            name='cromo_rep',
            field=models.ManyToManyField(to='test_project.Cromo_Rep'),
        ),
    ]
