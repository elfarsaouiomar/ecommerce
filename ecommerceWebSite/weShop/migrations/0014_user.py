# Generated by Django 2.2.13 on 2020-06-30 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weShop', '0013_subscribe_datedecreation'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('nom', models.TextField()),
            ],
        ),
    ]
