# Generated by Django 3.0 on 2020-06-12 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weShop', '0009_remove_order_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='country',
            field=models.OneToOneField(default='Maroc', on_delete=django.db.models.deletion.PROTECT, to='weShop.Country'),
        ),
    ]
