from django.contrib import admin
from.models import *

class OrderProductInlane(admin.TabularInline):
    model = ProductInOrder
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    inlines = [OrderProductInlane]

    class Meta:
        model = Order

admin.site.register(Order, OrderAdmin)


class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInOrder._meta.fields]

    class Meta:
        model = ProductInOrder

admin.site.register(ProductInOrder, ProductInOrderAdmin)


class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]

    class Meta:
        model = Status

admin.site.register(Status, StatusAdmin)


class BasketAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BasketModel._meta.fields]

    class Meta:
        model = BasketModel

admin.site.register(BasketModel, BasketAdmin)