from django.contrib import admin
from.models import *


# дополнительный класс который дает возможность просматривать и добавлять картинки в моделе Products,
# для работы необходимо в моделе ProductAdmin прописать inlines = [ProductImageInlane]


class CategoryProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CategoryProduct._meta.fields]


    class Meta:
        model = CategoryProduct

admin.site.register(CategoryProduct, CategoryProductAdmin)


class ProductImageInlane(admin.TabularInline):
    model = ProductImages
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImageInlane,]

    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)


class ProductImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductImages._meta.fields]


    class Meta:
        model = ProductImages

admin.site.register(ProductImages, ProductImageAdmin)

