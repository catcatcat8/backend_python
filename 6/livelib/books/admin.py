from django.contrib import admin
from books.models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'genre', 'release_year')
    list_filter = ('author', 'genre')

admin.site.register(Book, BookAdmin)
