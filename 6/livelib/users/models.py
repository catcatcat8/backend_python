from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(verbose_name='E-mail', unique=True)
    bio = models.TextField(verbose_name='Биография', max_length=500, blank=True)
    location = models.CharField(verbose_name='Город', max_length=30, blank=True)
    birthday = models.DateField(verbose_name='Дата рождения', null=True, blank=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
