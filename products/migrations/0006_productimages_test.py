# Generated by Django 2.1.2 on 2018-11-06 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20181106_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimages',
            name='test',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
