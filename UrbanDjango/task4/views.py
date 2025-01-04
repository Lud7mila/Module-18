from lib2to3.fixes.fix_input import context

from django.shortcuts import render


def get_cookbook(request):
    context = {"page_name": "Кулинарная книга"}
    return render(request, "Main.html", context)

def get_recipes(request):
    context = {"page_name": "Рецепты",
               'recipes': ['Завтрак "Малиновое искушение"',
                           'Торт "Тыквенное наслаждение"',
                           'Суп-пюре "Зимняя радость"',]}
    return render(request, "Content.html", context)

def get_info_about(request):
    context = {"page_name": "Об авторе Кулинарной книги"}
    return render(request, "About.html", context)