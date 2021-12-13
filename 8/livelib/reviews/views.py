from json.encoder import JSONEncoder
from django.db.models.query import QuerySet
from django.http.response import HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import get_object_or_404, render
from books.models import Book
from reviews.models import Review
from books.models import Book
from users.models import User
from django.template import loader
from django.urls import reverse
from rest_framework import viewsets
from rest_framework.response import Response
from reviews.serializers import ReviewSerializer
import datetime

class ReviewViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Review.objects.all()
        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        querySet = Review.objects.all()
        review = get_object_or_404(querySet, pk=pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

def index(request):
    header = "LIVELIB"                
    menu = {
        "add" : "Добавить рецензию",
        "edit" : "Редактировать рецензию",
        "delete": "Удалить рецензию",
        "list" : "Список рецензий",
        "search" : "Поиск рецензий",
        "hello" : "Привет, гость!"
    }
    main = "Книжный форум"
    footer = "Лебедев Евгений: Backend-разработка на Python ДЗ #6"
 
    data = {"header": header, "menu": menu, "main": main, "footer": footer}
    return render(request, "index.html", context=data)


def create_review_add_form(request):
    name = "Книга"
    author = "Автор"
    score = "Оценка"
    review = "Отзыв"
    user = "Пользователь"
    data = {"name": name, "author": author, "score": score, "review" : review, "user": user}
    return render(request, "form.html", context=data)

def create_review(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        author = request.POST.get('author')
        score = request.POST.get('score')
        review_text = request.POST.get('review')
        user = request.POST.get('user')
        created_at = str(datetime.datetime.now())

        serializer = ReviewSerializer(data={'book': name, 'review': review_text, 'rating': score, 'created_at': created_at, 'user': user})
        try:
            book_obj = Book.objects.get(name=name, author=author)
            user_obj = User.objects.get(username=user)
        except Book.DoesNotExist:
            return HttpResponseBadRequest("Не найдена книга")
        except User.DoesNotExist:
            return HttpResponseBadRequest("Не найден пользователь")
        else:
            if serializer.is_valid():
                Review.objects.create(book=book_obj, review=review_text, rating=score, created_at=created_at, user=user_obj)
                return JsonResponse(request.POST, json_dumps_params={"ensure_ascii": False})
            else:
                return HttpResponseBadRequest(f'Incorrect field: {serializer.errors}')
    else:
        return HttpResponseNotAllowed(['POST'])
    

def search_review(request):
    if request.method == 'GET':
        if request.GET.get('id') and request.GET.get('id').isdigit() and 0 <= int(request.GET.get('id')) <= 2:
            return JsonResponse(database[int(request.GET['id'])])
        else:
            return JsonResponse({'Name': 'Dead souls', 'Score' : '9.3/10', 'Review': 'Great book!'})
    else:
        return HttpResponseNotAllowed(['GET'])

def review_list(request):
    if request.method == 'GET':
        reviews = Review.objects.filter()
        data = [
            {
                "ID рецензии": review.id,
                'Книга': review.book.name,
                'Автор': review.book.author,
                'Отзыв': review.review,
                'Оценка': review.rating,
                'Пользователь': review.user.username
            } for review in reviews
        ]
        return JsonResponse({'Отзывы': data}, json_dumps_params={"ensure_ascii": False})
    else:
        return HttpResponseNotAllowed(['GET'])

def create_review_edit_form(request):
    book = "Название книги"
    author = "Автор"
    user = "Пользователь"
    new_text = "Новый текст"
    new_score = "Новая оценка"
    data = {"book": book, "author": author, "user": user, "new_text": new_text, "new_score": new_score}
    return render(request, "edit_form.html", context=data)

def edit_review(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        author = request.POST.get('author')
        user = request.POST.get('user')
        text = request.POST.get('new_text')
        score = request.POST.get('new_score')
        update = str(datetime.datetime.now())

        try:
            review_obj = Review.objects.filter(book__name=name, book__author=author, user__username=user)
        except Review.DoesNotExist:
            return HttpResponseBadRequest("Не найдена рецензия")
        else:
            review_obj.update(review=text, rating=score, updated_at=update)
            return JsonResponse(request.POST, json_dumps_params={"ensure_ascii": False})
    else:
        return HttpResponseNotAllowed(['POST'])

def review_delete_form(request):
    book = "Название книги"
    author = "Автор"
    user = "Пользователь"
    method = "post"
    value = "Удалить рецензию"
    data = {"book": book, "author": author, "user": user, "method": method, "value": value}
    return render(request, "delete_form.html", context=data)

def delete_review(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        author = request.POST.get('author')
        user = request.POST.get('user')

        try:
            review_obj = Review.objects.get(book__name=name, book__author=author, user__username=user)
        except Review.DoesNotExist:
            return HttpResponseBadRequest(f'Не найден отзыв пользователя {user} на книгу {name} автора {author}')
        else:
            review_obj.delete()
            return JsonResponse(request.POST, json_dumps_params={"ensure_ascii": False})
    else:
        return HttpResponseNotAllowed(['POST'])

def review_search_form(request):
    title = "Детальное отображение"
    text = "Напишите в url: http://localhost:8000/search/{id рецензии}"
    data = {"title": title, "text": text}
    return render(request, "search.html", context=data)

def review_detail(request, review_id=None):
    if request.method == 'GET':
        try:
            review = Review.objects.get(id=review_id)
        except Review.DoesNotExist:
            return HttpResponseBadRequest(f'Не найден отзыв с таким id')
        else:
            data = {
                "Название книги": review.book.name,
                "Автор": review.book.author,
                "Жанр": review.book.genre,
                "Год издания": review.book.release_year,
                "Текст рецензии": review.review,
                "Оценка": review.rating,
                "Дата создания рецензии": review.created_at,
                "Дата последнего обновления": review.updated_at,
                "Имя пользователя": review.user.username,
                "Email пользователя": review.user.email,
                "Биография пользователя": review.user.bio,
                "Город рождения пользователя": review.user.location,
                "День рождения пользователя": review.user.birthday
            }
            return JsonResponse(data, json_dumps_params={"ensure_ascii": False})
    else:
        return HttpResponseNotAllowed(['GET'])

def my_reviews(request):
    if request.method == 'GET':
        user_reviews = Review.objects.filter(user__username=request.user.username)
        if user_reviews:
            data = [
                {
                    "ID рецензии": review.id,
                    'Книга': review.book.name,
                    'Автор': review.book.author,
                    'Отзыв': review.review,
                    'Оценка': review.rating,
                } for review in user_reviews
            ]
            return JsonResponse({f'Отзывы пользователя {request.user.username}': data}, json_dumps_params={"ensure_ascii": False})
        else:
            return HttpResponseBadRequest(f'Пользователь {request.user} еще не добавил ни одного отзыва!')
    else:
        return HttpResponseNotAllowed(['GET'])
