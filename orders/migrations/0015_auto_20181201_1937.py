# Generated by Django 2.1.2 on 2018-12-01 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_basketmodel_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basketmodel',
            name='number',
            field=models.IntegerField(default=1),
        ),
    ]
