# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-18 22:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_project', '0011_auto_20180418_1703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cromo',
            name='cromo_rep',
        ),
        migrations.AddField(
            model_name='cromo',
            name='cromo_rep',
            field=models.ManyToManyField(to='test_project.Cromo_Rep'),
        ),
    ]
