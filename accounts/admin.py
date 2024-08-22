from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


class ClientAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('phone_number', 'email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'address')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'password1', 'password2'),
        }),
    )
    list_display = ('phone_number', 'first_name', 'address', 'is_staff')
    search_fields = ('phone_number', 'first_name', 'last_name', 'address')
    ordering = ('phone_number',)


admin.site.register(get_user_model(), ClientAdmin)
