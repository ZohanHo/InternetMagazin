# Generated by Django 2.1.2 on 2018-11-10 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimages',
            name='image_product',
            field=models.ImageField(upload_to=''),
        ),
    ]
