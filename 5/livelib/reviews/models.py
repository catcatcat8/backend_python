from django.db import models
from books.models import Books
from users.models import Users

class Reviews(models.Model):
    book_id = models.ForeignKey(Books, on_delete=models.PROTECT, verbose_name="Идентификатор книги")
    review = models.TextField(verbose_name="Рецензия на книгу")
    rating = models.IntegerField(verbose_name="Оценка книги")
    created_at = models.DateTimeField(verbose_name="Дата и время создания рецензии")
    updated_at = models.DateTimeField(null=True, blank=True, verbose_name="Дата и время обновления рецензии")
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name="Идентификатор пользователя")
