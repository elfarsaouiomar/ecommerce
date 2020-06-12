# Generated by Django 3.0 on 2020-06-12 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weShop', '0007_order_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='weShop.Country'),
        ),
    ]
