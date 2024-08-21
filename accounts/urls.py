from django.contrib.auth.views import LogoutView
from django.urls import path

from accounts.views import register_user, login_user

app_name = 'accounts'

urlpatterns = [
    path('register', register_user, name='register'),
]

urlpatterns += [
    path('login', login_user, name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]
