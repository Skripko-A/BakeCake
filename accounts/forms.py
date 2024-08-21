from django import forms
from django.contrib.auth import get_user_model
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import RegionalPhoneNumberWidget

User = get_user_model()


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('phone_number', 'first_name', 'email')


class UserLoginForm(forms.Form):
    phone_number = PhoneNumberField(
        widget=RegionalPhoneNumberWidget()
    )
