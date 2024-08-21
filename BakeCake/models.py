from django.db import models
from django.db.models import ForeignKey, SET_NULL, PROTECT
from phonenumber_field.modelfields import PhoneNumberField

from accounts.models import Client


class Topping(models.Model):
    title = models.CharField(max_length=25, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=100)

    def __str__(self):
        return f'{self.title}'

class Berrie(models.Model):
    title = models.CharField(max_length=25, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=100)

    def __str__(self):
        return f'{self.title}'

class Decor(models.Model):
    title = models.CharField(max_length=25, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=100)

    def __str__(self):
        return f'{self.title}'


class Cake(models.Model):
    shapes = {'ROUND': 'круг', 'SQUARE':'квадрат', 'RECTANGLE': 'прямоугольник'}
    title = models.CharField(max_length=25, verbose_name='Название')
    image = models.ImageField(upload_to='images/cakes', verbose_name='Картинка')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    levels_number = models.PositiveIntegerField(verbose_name=' Количество уровней (1, 2, 3')
    shape = models.CharField(choices=shapes, max_length=25, verbose_name='Форма (круг, квадрат, прямоугольник')
    topping = models.ForeignKey(Topping, verbose_name='Топпинг', on_delete=models.SET_NULL,
                                related_name='cakes', null=True, blank=True)
    berrie = models.ForeignKey(Berrie, verbose_name='Ягода', on_delete=models.SET_NULL,
                               related_name='cakes', null=True, blank=True)
    decor = models.ForeignKey(Decor, verbose_name='Декор', on_delete=models.SET_NULL,
                              related_name='cakes', null=True, blank=True)
    inscription = models.CharField(max_length=25, verbose_name='Надпись', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=100)

    def __str__(self):
        return f'{self.title}'


class Order(models.Model):
    cake = ForeignKey(Cake, verbose_name='Торт', on_delete=PROTECT, related_name='orders')
    customer = ForeignKey(Client, verbose_name='Клиент', on_delete=models.CASCADE, related_name='orders')
    address = models.TextField(verbose_name='Адрес доставки')
    date = models.DateField(verbose_name='Дата')
    phone = PhoneNumberField(unique=True)

    def __str__(self):
        return f'{self.cake}{self.customer}'