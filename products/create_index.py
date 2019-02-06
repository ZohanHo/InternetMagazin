from django.core.management.base import BaseCommand, CommandError
from products.models import Product, CategoryProduct
from orders.models import *
from elasticsearch import Elasticsearch


class Command(BaseCommand):

    def hendle(self, *args, **kwargs):


        for foo in Product.objects.all(): # выгребаем все с Продукт
            es = Elasticsearch()
            if foo.category:
                slug = foo.category.name  # Слиг равен пк категории
            else:
                continue

            if foo.images:
                images = foo.images.url
            else:
                images = ''

            doc = {
                "name":foo.product_name,
                "price":foo.price,
                "dicriptions":foo.discription_product,
                "pk":foo.pk,
                "slug":foo.slug,
                "image": images,
                "propertis": foo.get_filters_lol(),
                }

            res = es.index(index=slug, doc_type="prod",  id=foo.id, body=doc)
            print(res)