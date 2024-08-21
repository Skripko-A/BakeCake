from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class ClientManager(BaseUserManager):
    def _create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('Phone number must be set')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone_number, password, **extra_fields)

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self._create_user(phone_number, password, **extra_fields)


class Client(AbstractUser):
    username = None
    first_name = models.CharField(
        verbose_name='имя',
        max_length=50
    )
    phone_number = PhoneNumberField(
        verbose_name='номер телефона',
        unique=True,
        db_index=True
    )
    email = models.EmailField(
        verbose_name='электронная почта',
        unique=True,
        db_index=True
    )

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = ClientManager()

    class Meta:
        db_table = 'auth_user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        if self.first_name:
            return self.first_name
        return str(self.phone_number)
