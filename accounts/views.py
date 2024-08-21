from django.contrib.auth import get_user_model, login
from django.db import transaction
from django.shortcuts import redirect, render
from django.urls import reverse

from accounts.forms import UserRegisterForm, UserLoginForm

User = get_user_model()


def login_user(request, errors=None):
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if not form.is_valid():
            errors = form.errors
            return render(request,
                          'accounts/login.html',
                          context={'errors': errors})
        user_data = form.cleaned_data
        try:
            user = User.objects.get(phone_number=user_data['phone_number'])
        except User.DoesNotExist:
            user = None
            errors = {'user': ['Пользователь не найден.']}

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
    return render(request, 'accounts/login.html', context={'errors': errors})


@transaction.atomic()
def register_user(request, errors=None):
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if not form.is_valid():
            errors = form.errors
            return render(request,
                          'accounts/register.html',
                          context={'errors': errors})

        user_data = form.cleaned_data
        phone_number = user_data.pop('phone_number')
        first_name = user_data.pop('first_name')
        email = user_data.pop('email')

        if not User.objects.filter(phone_number=phone_number) \
           and not User.objects.filter(email=email):
            user = User.objects.create_user(
                phone_number=phone_number,
                email=email,
                first_name=first_name
            )
        if user.is_active:
            login(request, user)
            return redirect('/')

        return redirect(reverse('accounts:login'))

    return render(request,
                  'accounts/register.html',
                  context={'errors': errors})
