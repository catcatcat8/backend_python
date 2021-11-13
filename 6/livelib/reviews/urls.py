from django.contrib import admin
from django.urls import path
from reviews.views import index, review_detail, review_search_form, search_review, review_list, create_review_add_form, create_review, edit_review, create_review_edit_form, review_delete_form, delete_review

urlpatterns = [
    path('', index, name = 'index'),
    path('search/', review_search_form, name = 'review_search_form'),
    path('review_list/', review_list, name = "review_list"),
    path('add_review/', create_review_add_form, name = 'add_review'),
    path('add_review/added', create_review, name = 'create_review'),
    path('edit_review/', create_review_edit_form, name = 'edit_review'),
    path('edit_review/edited/', edit_review, name='edit_review'),
    path('delete_review/', review_delete_form, name='review_delete_form'),
    path('delete_review/deleted/', delete_review, name='delete_review'),
    path('search/<int:review_id>', review_detail, name='review_detail')
]