from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from .views import show_main


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_main),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
