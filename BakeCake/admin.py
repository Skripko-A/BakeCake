import logging
from urllib.parse import urlparse

from django.conf import settings
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.html import format_html
from environs import Env
import requests

from .models import Topping, Berry, Decor, Cake, Order, Layer, Shape, ReferalLink

env = Env()
env.read_env()

logger = logging.getLogger('ReferalLinkAdmin')
logger.setLevel(logging.INFO)
handler = logging.FileHandler('short_links_errors.log')
handler.setLevel(logging.INFO)
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
        ISHORTN_TOKEN = settings.ISHORTN_TOKEN
        headers = {'x-api-key': ISHORTN_TOKEN}
        for obj in queryset:
            try:
                parsed_url = urlparse(obj.link)
                if not parsed_url.scheme or not parsed_url.netloc or len(parsed_url.path.split('/')) < 4:
                    logger.error(f'Invalid URL format for link: {obj.link}')
                    continue
                short_link_alias = parsed_url.path.split('/')[3]
                url = f'https://ishortn.ink/api/v1/analytics/{short_link_alias}'
                logger.info(f'Fetching analytics for URL: {url}')
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    obj.visits = sum(response.json().get('clicksPerOS', {}).values())
                    obj.save()
                    logger.info(f'Successfully updated visits for {obj.link}')
                else:
                    logger.error(f'Error fetching clicks info for link: {response.status_code} - {response.text}')
            except Exception as e:
                logger.error(f'Exception occurred: {e}')

        return super().changelist_view(request, extra_context)

