# Generated by Django 2.1.2 on 2018-12-02 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_auto_20181201_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basketmodel',
            name='number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='basketmodel',
            name='price',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='basketmodel',
            name='session_key',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
