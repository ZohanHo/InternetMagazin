# Generated by Django 2.1.2 on 2018-11-20 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20181118_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcarmodel',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=True, to='products.CategoryProduct'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=True, to='products.CategoryProduct'),
        ),
        migrations.AlterField(
            model_name='product',
            name='discription_product',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='product_image',
            field=models.ForeignKey(blank=True, on_delete=True, related_name='images', to='products.Product'),
        ),
    ]
