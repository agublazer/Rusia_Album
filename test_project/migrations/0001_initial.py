# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-16 18:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cromo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('tipo', models.CharField(choices=[('Jugador', 'Jugador'), ('Miscaleneo', 'Miscaleneo')], default='Jugador', max_length=2)),
                ('descripcion_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pagina',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('tipo', models.CharField(choices=[('Pais', 'Pais'), ('MS', 'Miscaleneo')], default='Pais', max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='cromo',
            name='page_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_project.Pagina'),
        ),
    ]
