from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Topping, Berrie, Decor, Cake, Order


@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = ('title', )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'address', 'date')


@admin.register(Topping)
class ToppingAdmin(ModelAdmin):
    list_display = ('title',)


@admin.register(Berrie)
class BerrieAdmin(ModelAdmin):
    list_display = ('title',)


@admin.register(Decor)
class DecorAdmin(ModelAdmin):
    list_display = ('title',)