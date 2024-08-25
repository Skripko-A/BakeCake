from django.db import models
from django.db.models import ForeignKey, PROTECT
from phonenumber_field.modelfields import PhoneNumberField

from accounts.models import Client


class Topping(models.Model):
    title = models.CharField(max_length=25, verbose_name='Название')
    description = models.TextField(null=True,
                                   blank=True,
                                   verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=100)

    def __str__(self):
        return f'{self.title}'


class Berry(models.Model):
    title = models.CharField(max_length=25, verbose_name='Название')
    description = models.TextField(null=True,
                                   blank=True,
                                   verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=100)

    def __str__(self):
        return f'{self.title}'


class Decor(models.Model):
    title = models.CharField(max_length=25, verbose_name='Название')
    description = models.TextField(null=True,
                                   blank=True,
                                   verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=100)

    def __str__(self):
        return f'{self.title}'


class Shape(models.Model):
    shapes = {'ROUND': 'Круг',
              'SQUARE': 'Квадрат',
              'RECTANGLE': 'Прямоугольник'}
    title = models.CharField(choices=shapes,
                             max_length=25,
                             verbose_name='Форма')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=100)

    def __str__(self):
        return f'{self.title}'


class Layer(models.Model):
    number = models.PositiveIntegerField(verbose_name=' Количество уровней')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=100)

    def __str__(self):
        return f'{self.number}'


class Cake(models.Model):
    title = models.CharField(max_length=25, verbose_name='Название')
    image = models.ImageField(upload_to='images/cakes',
                              verbose_name='Картинка')
    description = models.TextField(null=True,
                                   blank=True,
                                   verbose_name='Описание')
    levels_number = models.ForeignKey(Layer,
                                      verbose_name='Количество уровней',
                                      on_delete=models.SET_NULL,
                                      related_name='cakes',
                                      null=True,
                                      blank=True)
    shape = models.ForeignKey(Shape,
                              verbose_name='Форма',
                              on_delete=models.SET_NULL,
                              null=True,
                              blank=True,
                              related_name='cakes')
    topping = models.ForeignKey(Topping,
                                verbose_name='Топпинг',
                                on_delete=models.SET_NULL,
                                related_name='cakes',
                                null=True,
                                blank=True)
    berry = models.ForeignKey(Berry,
                              verbose_name='Ягода',
                              on_delete=models.SET_NULL,
                              related_name='cakes',
                              null=True,
                              blank=True)
    decor = models.ForeignKey(Decor,
                              verbose_name='Декор',
                              on_delete=models.SET_NULL,
                              related_name='cakes',
                              null=True,
                              blank=True)
    inscription = models.CharField(max_length=25,
                                   verbose_name='Надпись',
                                   blank=True,
                                   null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=100)

    def __str__(self):
        return f'{self.title}'


class Order(models.Model):
    cake = ForeignKey(Cake,
                      verbose_name='Торт',
                      on_delete=PROTECT,
                      related_name='orders',
                      null=True,
                      blank=True)

    customer = ForeignKey(Client,
                          verbose_name='Клиент',
                          on_delete=models.CASCADE,
                          related_name='orders')
    name = models.CharField(max_length=255, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email', db_index=True)
    phone = PhoneNumberField(verbose_name='Номер телефона', db_index=True)
    address = models.TextField(verbose_name='Адрес доставки', db_index=True)
    date = models.DateField(verbose_name='Дата', db_index=True)
    time = models.TimeField(verbose_name='Время')

    levels_number = models.ForeignKey(Layer,
                                      verbose_name='Количество уровней',
                                      on_delete=models.SET_NULL,
                                      related_name='orders',
                                      null=True,
                                      blank=True)
    shape = models.ForeignKey(Shape,
                              verbose_name='Форма',
                              on_delete=models.SET_NULL,
                              null=True,
                              blank=True,
                              related_name='orders')
    topping = models.ForeignKey(Topping,
                                verbose_name='Топпинг',
                                on_delete=models.SET_NULL,
                                related_name='orders',
                                null=True,
                                blank=True)
    berry = models.ForeignKey(Berry,
                              verbose_name='Ягода',
                              on_delete=models.SET_NULL,
                              related_name='orders',
                              null=True,
                              blank=True)
    decor = models.ForeignKey(Decor,
                              verbose_name='Декор',
                              on_delete=models.SET_NULL,
                              related_name='orders',
                              null=True,
                              blank=True)
    inscription = models.CharField(max_length=25,
                                   verbose_name='Надпись',
                                   blank=True,
                                   null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    comment = models.TextField(null=True,
                               blank=True,
                               verbose_name='Комментарий к заказу')
    delivery_comment = models.TextField(null=True,
                                        blank=True,
                                        verbose_name='Комментарий к курьеру')

    def __str__(self):
        return f'{self.customer}, заказ №{self.id}'


class ReferalLink(models.Model):
    link = models.CharField(max_length=255)
    visits = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.link}: {self.visits}'
