# Generated by Django 4.2.13 on 2024-07-16 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_products_short_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='short_description',
            field=models.TextField(blank=True),
        ),
    ]