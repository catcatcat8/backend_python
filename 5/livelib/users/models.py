from django.db import models
from django.db.models.base import Model

class Users(models.Model):
    username = models.CharField(max_length=20, unique=True, verbose_name="Имя пользователя")
    email = models.EmailField(unique=True, verbose_name="Email пользователя")

    def __str__(self):
        return self.username

    class Meta:
        ordering = ('-username')
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
