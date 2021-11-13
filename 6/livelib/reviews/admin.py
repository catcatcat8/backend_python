from django.contrib import admin
from reviews.models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'review', 'rating', 'created_at', 'updated_at', 'user')
    list_filter = ('book', 'user')

admin.site.register(Review, ReviewAdmin)
