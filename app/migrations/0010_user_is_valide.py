# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-09 08:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20170307_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_valide',
            field=models.BooleanField(default=True),
        ),
    ]
