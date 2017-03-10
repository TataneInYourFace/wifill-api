# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-07 08:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20170306_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='zip',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='plate',
            field=models.CharField(max_length=255),
        ),
    ]
