from django.http.response import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render

database = [
        {'Name': 'War and piece', 'Score': '8.9/10', 'Review': 'Very good book...'},
        {'Name': 'Harry Potter', 'Score' : '9.5/10', 'Review': 'My favourite book'},
        {'Name': 'Master and Margarita', 'Score' : '7.7/10', 'Review': 'Interesting story'}
    ]

def index(request):
    header = "LIVELIB"                
    menu = {
        "add" : "Добавить рецензию",
        "my" : "Мои рецензии",
        "list" : "Список рецензий",
        "search" : "Поиск рецензий",
        "hello" : "Привет, гость!"
    }
    main = "Книжный форум"
    footer = "Лебедев Евгений: Backend-разработка на Python ДЗ #4"
 
    data = {"header": header, "menu": menu, "main": main, "footer": footer}
    return render(request, "index.html", context=data)


def add_review(request):
    name = "Книга"
    score = "Оценка"
    review = "Отзыв"
    data = {"name": name, "score": score, "review" : review}
    return render(request, "form.html", context=data)

def create_review(request):
    if request.method == 'POST':
        new_book = {
            'Name': request.POST.get('name'),
            'Score': request.POST.get('score'),
            'Review': request.POST.get('review')
        }
        database.append(new_book)
        return JsonResponse(request.POST)
    else:
        return HttpResponseBadRequest()
    

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
        return JsonResponse(database, safe=False)
    else:
        return HttpResponseBadRequest()


