from json.encoder import JSONEncoder
from django.http.response import HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render
from books.models import Book
from reviews.models import Review
from books.models import Book
from users.models import User
from django.template import loader
from django.urls import reverse
import datetime

database = [
        {'Name': 'War and piece', 'Score': '8.9/10', 'Review': 'Very good book...'},
        {'Name': 'Harry Potter', 'Score' : '9.5/10', 'Review': 'My favourite book'},
        {'Name': 'Master and Margarita', 'Score' : '7.7/10', 'Review': 'Interesting story'}
    ]

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

        try:
            book_obj = Book.objects.get(name=name, author=author)
            user_obj = User.objects.get(username=user)
        except Book.DoesNotExist:
            return HttpResponseBadRequest("Не найдена книга")
        except User.DoesNotExist:
            return HttpResponseBadRequest("Не найден пользователь")
        else:
            Review.objects.create(book=book_obj, review=review_text, rating=score, created_at=created_at, user=user_obj)
            return JsonResponse(request.POST, json_dumps_params={"ensure_ascii": False})
    else:
        return HttpResponseNotAllowed
    

def search_review(request):
    if request.method == 'GET':
        if request.GET.get('id') and request.GET.get('id').isdigit() and 0 <= int(request.GET.get('id')) <= 2:
            return JsonResponse(database[int(request.GET['id'])])
        else:
            return JsonResponse({'Name': 'Dead souls', 'Score' : '9.3/10', 'Review': 'Great book!'})
    else:
        return HttpResponseBadRequest()

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
        return HttpResponseNotAllowed

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
        return HttpResponseNotAllowed("Неправильный метод")

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
        return HttpResponseNotAllowed('Нужно использовать метод POST')

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
        return HttpResponseNotAllowed