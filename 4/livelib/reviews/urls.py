from django.contrib import admin
from django.urls import path
from reviews.views import index, search_review, review_list, add_review, create_review

urlpatterns = [
    path('', index, name = 'index'),
    path('search/', search_review, name = 'search_review'),
    path('review_list/', review_list, name = "review_list"),
    path('add_review/', add_review, name = 'add_review'),
    path('add_review/added', create_review, name = 'create_review')
]