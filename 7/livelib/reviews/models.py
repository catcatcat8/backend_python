from django.db import models
from books.models import Book
from users.models import User

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Идентификатор книги")
    review = models.TextField(verbose_name="Рецензия на книгу")
    rating = models.IntegerField(verbose_name="Оценка книги")
    created_at = models.DateTimeField(verbose_name="Дата и время создания рецензии", blank=True, null=False)
    updated_at = models.DateTimeField(null=True, blank=True, verbose_name="Дата и время обновления рецензии")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Идентификатор пользователя")

    def __str__(self):
        return self.review

    class Meta:
        unique_together = ('book', 'user',)
        ordering = ('-created_at',)
        verbose_name = 'Рецензия'
        verbose_name_plural = 'Рецензии'
