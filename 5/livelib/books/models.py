from django.db import models

class Books(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name="Название книги")
    author = models.TextField(null=True, blank=True, verbose_name="Автор(-ы) книги")
    genre = models.CharField(max_length=32, null=True, blank=True, verbose_name="Жанр книги")
    release_year = models.IntegerField(null=True, blank=True, verbose_name="Год издания книги")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
