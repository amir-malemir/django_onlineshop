# Generated by Django 4.2.13 on 2024-07-14 10:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_products_cover_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='datetime_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
