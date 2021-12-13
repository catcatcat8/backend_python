from django.contrib import admin
from django.urls import path
from reviews.views import index
from users.views import UserViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api', UserViewSet, basename="users")

urlpatterns = [
    path('', index, name = 'index'),
]

urlpatterns += router.urls