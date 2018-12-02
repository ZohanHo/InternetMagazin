from django.db import models
from django.shortcuts import reverse



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




    def __str__(self):
        return "{}".format(self.product_name)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class ProductImages(models.Model):
    image_product = models.ImageField(upload_to="")
    product_image = models.ForeignKey(Product, related_name="images", on_delete=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    is_active = models.BooleanField(default=True)



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

    def get_absolute_url(self):  # метод который возвращает ссылку на конкретный обьет класса, передаем url шаблона и словарь
        return reverse("detail_new_car_url", kwargs={"pk": self.pk})  # в словарь в качестве ключа получает поле,
        # то поле по которому мы проводим идентификацию обьекта и self.slug (поле конкретно обьекта )

    # url для tag_update_url
    def get_abs_update_url(self):  #
        return reverse("update_car_url", kwargs={"pk": self.pk})

    # url для post_del_url
    def get_abs_del_url(self):  #
        return reverse("delete_car_url", kwargs={"pk": self.pk})


