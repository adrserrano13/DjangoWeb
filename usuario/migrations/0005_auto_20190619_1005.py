# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-06-19 10:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0004_restaurante'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurante',
            name='id',
        ),
        migrations.AlterField(
            model_name='restaurante',
            name='nombre',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
