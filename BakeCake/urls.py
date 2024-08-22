from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from .views import show_main, show_lk, show_lk_order, cakes_catalog, cake_page, create_custom_cake_order


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_main, name='show_main'),
    path('cakes_catalog', cakes_catalog, name='cakes_catalog'),
    path('cake/<int:cake_id>', cake_page, name='cake_page'),
    path('lk', show_lk, name='show_lk'),
    path('lk-order', show_lk_order, name='show_lk-order'),
    path('create_custom_cake_order', create_custom_cake_order, name='create_custom_cake_order'),
    path('', include('accounts.urls', namespace='accounts')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
