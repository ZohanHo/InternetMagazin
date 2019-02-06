from products.models import Product, ProductImages, CategoryProduct
import scrapy
from django.utils.text import slugify
from django.conf import settings
import time


class CategoryProductSpider(scrapy.Spider):
    name = "category_products"  # идентифицирует паука. Он должен быть уникальным в рамках проекта,

    # то есть нельзя устанавливать одно и то же имя для разных пауков.

    def start_requests(self):  # должен возвращать итерируемое количество запросов
        urls = [
            # 'http: // localhost: 8000 /',
            'http: // localhost: 8000 /?page = 2',
        ]

        # for category in CategoryProduct.objects.all():

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # метод, который будет вызываться для обработки загруженного ответа на каждый сделанный запрос.
        # Параметр response является экземпляром, TextResponseкоторый содержит содержимое страницы и имеет
        # дополнительные полезные методы для его обработки.
        page = response.url.split("/")[-2]
        product = "localhost: 8000 /".format(page)
        with open(product, 'wb') as file:
            file.write(response.body)
        self.log("Saved file".format(product))
