from django.db import models
from orders.models import *
from django.shortcuts import reverse
from django.contrib.auth.models import User



class CategoryProduct(models.Model):
    name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.name)


    class Meta:
        verbose_name = "Категория товара"
        verbose_name_plural = "категория товаров"


class Product(models.Model):

    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discription_product = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    is_active = models.BooleanField(default=True)
    discount = models.IntegerField(default=0, blank=True)
    # on_delete=models.CASCADE - все поля всязаные тоже удалятся или добавятся (тянет в базе всю последовательность)
    category = models.ForeignKey(CategoryProduct, on_delete=True, blank=True, null=True)
    #basket = models.ForeignKey(BasketModel, on_delete=True, blank=True, null=True)

    #добавить user в админку
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, default=True, null=True) # Также необходимо импортировать - from django.contrib.auth.models import User
    #basket = models.ForeignKey(BasketModel, on_delete=models.CASCADE, blank=False, default=True, null=True) # Также необходимо импортировать - from django.contrib.auth.models import User
    likes = models.IntegerField(default=0, blank=True, null=True)
    likedone = models.ManyToManyField(User, blank=True, related_name='users_video_main')


    def __str__(self):
        return "{}".format(self.product_name)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    # лайки
    def get_absolute_url_likes(self):  # метод который возвращает ссылку на конкретный обьет класса, передаем url шаблона и словарь
        return reverse("likes_url", kwargs={"pk": self.pk})  # в словарь в качестве ключа получает поле,
        # то поле по которому мы проводим идентификацию обьекта и self.slug (поле конкретно обьекта )

    # Добавление продукта с лендинговой страницы в корзину
    def get_absolute_url_base(self):  # метод который возвращает ссылку на конкретный обьет класса, передаем url шаблона и словарь
        return reverse("add_product_base_url", kwargs={"pk": self.pk})  # в словарь в качестве ключа получает поле,
        # то поле по которому мы проводим идентификацию обьекта и self.slug (поле конкретно обьекта )



class ProductImages(models.Model):
    image_product = models.ImageField(upload_to="")
    product_image = models.ForeignKey(Product, related_name="images", on_delete=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    is_active = models.BooleanField(default=True)


    # Деталка продукта основного
    def get_absolute_url_product(self):  # метод который возвращает ссылку на конкретный обьет класса, передаем url шаблона и словарь
        return reverse("product_detail_url", kwargs={"pk": self.pk})  # в словарь в качестве ключа получает поле,
        # то поле по которому мы проводим идентификацию обьекта и self.slug (поле конкретно обьекта )

    class Meta:
        verbose_name = "Картинка"
        verbose_name_plural = "Картинки"

class AddCarModel(models.Model):

    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discription_product = models.TextField()
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(CategoryProduct, on_delete=True, blank=True, null=True)
    image_product = models.ImageField(upload_to = "image_new_car/", blank=True)

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"


    # деталка частных автомобилей
    def get_absolute_url(self):  # метод который возвращает ссылку на конкретный обьет класса, передаем url шаблона и словарь
        return reverse("detail_new_car_url", kwargs={"pk": self.pk})  # в словарь в качестве ключа получает поле,
        # то поле по которому мы проводим идентификацию обьекта и self.slug (поле конкретно обьекта )

    #  редактирование обьявления о продаже
    def get_abs_update_car_url(self):  # Редактироварие частного обьявлений
        return reverse("update_car_url", kwargs={"pk": self.pk})

    # удаление обьявления о продаже
    def get_abs_del_url(self):  # Удаление из корзины
        return reverse("delete_car_url", kwargs={"pk": self.pk})

    # url для tag_update_url
    def get_abs_update_num_url(self):  # Редактирование количкства в корзине
        return reverse("change_number_url_update", kwargs={"pk": self.pk})