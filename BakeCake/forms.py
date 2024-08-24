from django import forms
from django.utils import timezone

from .models import Order


class OrderRegularCakeForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('name', 'email', 'phone', 'address',
                  'date', 'time', 'comment', 'delivery_comment')

    def clean_date(self):
        date = self.cleaned_data.get('date')
        today = timezone.now().date()
        if date and date < today:
            raise forms.ValidationError(
                'Дата не может быть раньше сегодняшней.'
            )
        return date

    def clean_time(self):
        time = self.cleaned_data.get('time')
        if time and not (10 <= time.hour <= 23):
            raise forms.ValidationError(
                'Время должно быть между 10:00 и 23:00'
            )
        return time
