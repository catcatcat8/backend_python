from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponseNotAllowed
from application.settings import LOGIN_URL


def need_login(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        return redirect(LOGIN_URL)
    return wrapper


@need_login
def main(request):
    if request.method == 'GET':
        header = "LIVELIB"                
        menu = {
            "add" : "Добавить рецензию",
            "edit" : "Редактировать рецензию",
            "delete": "Удалить рецензию",
            "list" : "Список рецензий",
            "search" : "Поиск рецензий",
            "my" : "Мои рецензии",
            "hello" : f"Привет, {request.user.username}!"
        }
        main = "Книжный форум"
        footer = "Лебедев Евгений: Backend-разработка на Python ДЗ #8"
    
        data = {"header": header, "menu": menu, "main": main, "footer": footer}
        return render(request, "index.html", context=data)
    return HttpResponseNotAllowed('Not Allowed')

def login(request):
    return render(request, 'login.html')
