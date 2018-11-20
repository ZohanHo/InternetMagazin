from django.db import models
from products.models import *
from django.db.models.signals import post_save
from products.models import *

class Status(models.Model):

    name_status = models.CharField(max_length=30, blank=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.name_status

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


class Order(models.Model):
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # total price for products in order
    customer_name = models.CharField(max_length=50, blank=True)
    customer_email = models.EmailField(blank=True)
    customer_phone = models.CharField(max_length=50, blank=True)
    customer_address = models.CharField(max_length=150, blank=True)
    comments = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    is_active = models.BooleanField(default=True)
    status = models.ForeignKey(Status, blank=True, on_delete=True)


    def __str__(self):
        return "Заказ №{}, {}".format(self.id, self.status.name_status)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class ProductInOrder(models.Model):


    order = models.ForeignKey(Order, on_delete=True, blank=True)
    product = models.ForeignKey(Product, on_delete=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    is_active = models.BooleanField(default=True)
    nmb = models.IntegerField() # количество
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0) # цена за единицу товара
    total_price = models.DecimalField(max_digits=20, decimal_places=2,default=0) # price*nmb

    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        verbose_name = "Товар в заказе"
        verbose_name_plural = "Товары в заказе"

# Переопределяем метод save для модели который дубет созранять в админке поля с сумой заказа и общей сумой по всем заказам

    def save(self, *args, **kwargs):

        self.price_per_item = self.product.price # цена за единицу равняется цене в моделе Product.prise (цене товвара)
        self.total_price = self.price_per_item * self.nmb # общая цена равна (цена товара умножено на количество)

        super(ProductInOrder, self).save(*args, **kwargs)

# подсчет для общей сумы по всем позициям заказа, тут можем сохранять только не для текущей модели, так как будет вызван опять post_save
def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_product_in_order = ProductInOrder.objects.filter(order=order, is_active=True)

    order_total_price = 0
    for item in all_product_in_order:
        order_total_price += item.total_price

    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)

post_save.connect(product_in_order_post_save, sender=ProductInOrder)



class BasketModel(models.Model):

    #product = models.ForeignKey(Product, blank=True, null=True, on_delete=True)
    #order = models.ForeignKey(Order, blank=True, null=True, on_delete=True)
    session_key = models.CharField(max_length=120, null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discription_product = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(CategoryProduct, on_delete=True, blank=True, null=True)


    # def __str__(self):
    #     return "{}".format(self.product)

    class Meta:
        verbose_name = "Товар в корзине"
        verbose_name_plural = "Товары в корзине"

