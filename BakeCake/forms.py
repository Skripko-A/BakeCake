from django import forms

from .models import Order


class OrderRegularCakeForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('name', 'email', 'phone', 'address',
                  'date', 'time', 'comment', 'delivery_comment')
