# Generated by Django 2.1.3 on 2018-11-02 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=50)),
                ('customer_email', models.EmailField(blank=True, max_length=254)),
                ('customer_phone', models.CharField(blank=True, max_length=50)),
                ('comments', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='ProductInOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('order', models.ForeignKey(blank=True, on_delete=True, to='orders.Order')),
                ('product', models.ForeignKey(blank=True, on_delete=True, to='products.Product')),
            ],
            options={
                'verbose_name': 'Товар в заказе',
                'verbose_name_plural': 'Товары в заказе',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_status', models.CharField(blank=True, max_length=30)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(blank=True, on_delete=True, to='orders.Status'),
        ),
    ]