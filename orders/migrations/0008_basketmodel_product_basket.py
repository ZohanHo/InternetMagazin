# Generated by Django 2.1.2 on 2018-11-22 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_auto_20181120_1721'),
        ('orders', '0007_auto_20181120_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='basketmodel',
            name='product_basket',
            field=models.ForeignKey(blank=True, null=True, on_delete=True, to='products.Product'),
        ),
    ]
