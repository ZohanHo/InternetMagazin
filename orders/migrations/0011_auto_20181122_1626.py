# Generated by Django 2.1.2 on 2018-11-22 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20181122_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basketmodel',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
