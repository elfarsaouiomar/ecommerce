# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-25 22:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weShop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribe',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
