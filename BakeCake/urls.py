from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from .views import show_main, show_lk, show_lk_order


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_main, name='show_main'),
    path('lk', show_lk, name='show_lk'),
    path('lk-order', show_lk_order, name='show_lk-order')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
