# Generated by Django 2.1.2 on 2018-12-08 17:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_auto_20181208_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='likedone',
            field=models.ManyToManyField(blank=True, related_name='users_video_main', to=settings.AUTH_USER_MODEL),
        ),
    ]
