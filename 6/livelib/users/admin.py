from django.contrib import admin
from users.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'location', 'birthday')
    list_filter = ('location',)

admin.site.register(User, UserAdmin)
