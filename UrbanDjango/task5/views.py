from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .forms import UserRegister


def is_data_form_valid(username, password, repeat_password, age):
    info = {}
    users = ['Luda', "Tom", "Anna"]
    if username in users:
        info["error"] = f"Пользователь '{username}' уже существует!"
    if password != repeat_password:
        if not info:
            info["error"] = ''
        info['error'] = '\n'.join([info['error'], 'Пароли не совпадают!'])
    if age < 18:
        if not info:
            info["error"] = ''
        info["error"] = '\n'.join([info['error'], 'Вы должны быть старше 18!'])
    return info


def sign_up_by_django(request):
    info = {}
    form = UserRegister()

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            repeat_password = form.cleaned_data["repeat_password"]
            age = int(form.cleaned_data["age"])

            info = is_data_form_valid(username, password, repeat_password, age)

            if not info:
                return HttpResponse(f'Приветствуем, {username}!')
        else:
            form = UserRegister()

    return render(request, "registration_page.html", {'form': form, "info": info})


def sign_up_by_html(request: HttpRequest):
    info = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        info = is_data_form_valid(username, password, repeat_password, age)

        if not info:
            return HttpResponse(f'Приветствуем, {username}!')

    return render(request, "registration_page.html", {'info': info})