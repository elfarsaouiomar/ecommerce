# Generated by Django 3.0 on 2020-06-12 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weShop', '0005_auto_20200612_1020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='country',
        ),
    ]