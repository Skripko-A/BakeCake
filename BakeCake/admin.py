from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import Topping, Berry, Decor, Cake, Order, Shape, Layer


@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_preview')

    def get_preview(self, obj):
        return format_html('<img src="{}" style="max-width:300px; max-height:200px"/>', obj.image.url)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'address', 'date')


@admin.register(Topping)
class ToppingAdmin(ModelAdmin):
    list_display = ('title', 'price')


@admin.register(Berry)
class BerryAdmin(ModelAdmin):
    list_display = ('title', 'price')


@admin.register(Decor)
class DecorAdmin(ModelAdmin):
    list_display = ('title', 'price')


@admin.register(Shape)
class ShapeAdmin(ModelAdmin):
    list_display = ('title', 'price')

    def get_shape(self, obj):
        return obj.get_title_display()


@admin.register(Layer)
class LayerAdmin(ModelAdmin):
    list_display = ('number', 'price')
