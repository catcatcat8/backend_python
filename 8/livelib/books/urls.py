from django.contrib import admin
from django.urls import path
from reviews.views import index
from books.views import BookViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api', BookViewSet, basename="books")

urlpatterns = [
    path('', index, name = 'index'),
]

urlpatterns += router.urls