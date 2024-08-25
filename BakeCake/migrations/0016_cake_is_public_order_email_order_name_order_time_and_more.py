# Generated by Django 5.1 on 2024-08-22 13:03

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BakeCake', '0015_alter_layer_number_alter_shape_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='cake',
            name='is_public',
            field=models.BooleanField(db_index=True, default=False, verbose_name='Отображать в каталоге'),
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(db_index=True, default='', max_length=254, verbose_name='Email'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(default='', max_length=255, verbose_name='Имя'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='time',
            field=models.TimeField(default='12:00', verbose_name='Время'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cake',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/cakes', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.TextField(db_index=True, verbose_name='Адрес доставки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(db_index=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(db_index=True, max_length=128, region=None, verbose_name='Номер телефона'),
        ),
    ]
