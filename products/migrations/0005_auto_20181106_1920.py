# Generated by Django 2.1.2 on 2018-11-06 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20181106_1823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimages',
            name='product',
        ),
        migrations.AddField(
            model_name='productimages',
            name='product_image',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.Product'),
            preserve_default=False,
        ),
    ]
