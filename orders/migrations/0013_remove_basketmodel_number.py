# Generated by Django 2.1.2 on 2018-11-22 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_basketmodel_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basketmodel',
            name='number',
        ),
    ]
