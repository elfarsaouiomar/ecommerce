# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-28 14:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weShop', '0003_auto_20200428_1348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='size',
            name='id',
        ),
        migrations.AlterField(
            model_name='size',
            name='size',
            field=models.CharField(max_length=40, primary_key=True, serialize=False),
        ),
    ]
