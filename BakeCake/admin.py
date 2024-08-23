import logging

from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.html import format_html
import requests

from .models import Topping, Berry, Decor, Cake, Order, Layer, Shape, ReferalLink


BITLY_ACCESS_TOKEN = '8bcc2d5f4de46a50c78db56704093ce7c41f643c'

logger = logging.getLogger('ReferalLinkAdmin')
logger.setLevel(logging.INFO)
handler = logging.FileHandler('bitly_errors.log')
handler.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

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


@admin.register(Layer)
class LayerAdmin(ModelAdmin):
    list_display = ('number', 'price')


@admin.register(ReferalLink)
class ReferalLinkAdmin(admin.ModelAdmin):
    list_display = ('link', 'visits')

    def changelist_view(self, request, extra_context=None):
        queryset = self.get_queryset(request)
        headers = {
            'Authorization': f'Bearer {BITLY_ACCESS_TOKEN}',
        }
        for obj in queryset:
            try:
                bitly_link = obj.link
                if bitly_link.startswith('http'):
                    bitly_link_id = bitly_link.replace('https://', '').replace('http://', '').replace('/', '')
                else:
                    bitly_link_id = bitly_link

                bitly_url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitly_link_id}/clicks/summary'

                response = requests.get(bitly_url, headers=headers)
                if response.status_code == 200:
                    data = response.json()
                    obj.visits = data.get('total_clicks', 0)
                    obj.save()
                    logger.info(f'Successfully updated visits for {bitly_link}')
                else:
                    logger.error(f"Ошибка получения данных по ссылке {bitly_link_id}: {response.status_code}")
                    logger.error(response.json())
            except Exception as e:
                logger.error(f"Исключение при обработке ссылки {bitly_link}: {e}")

        return super().changelist_view(request, extra_context)
