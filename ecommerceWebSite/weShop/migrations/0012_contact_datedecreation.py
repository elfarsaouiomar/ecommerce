# Generated by Django 3.0 on 2020-06-15 09:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('weShop', '0011_auto_20200615_0946'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='dateDeCreation',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
