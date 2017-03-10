# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-07 14:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_order_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.ForeignKey(db_column='address_id', on_delete=django.db.models.deletion.CASCADE, to='app.Address'),
        ),
    ]
