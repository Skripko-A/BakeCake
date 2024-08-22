# Generated by Django 5.1 on 2024-08-22 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BakeCake', '0016_cake_is_public_order_email_order_name_order_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_comment',
            field=models.TextField(blank=True, null=True, verbose_name='Комментарий к курьеру'),
        ),
        migrations.AlterField(
            model_name='cake',
            name='image',
            field=models.ImageField(blank=True, default='images/cakes/Cake.png', null=True, upload_to='images/cakes', verbose_name='Картинка'),
        ),
    ]
