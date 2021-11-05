from django.db import models
from django.db.models.base import Model

class Users(models.Model):
    username = models.CharField(max_length=20, unique=True, verbose_name="Имя пользователя")
    email = models.EmailField(unique=True, verbose_name="Email пользователя")
