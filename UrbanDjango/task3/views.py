from django.shortcuts import render
from django.views import View

class CookBook(View):
    def get(self, request):
        return render(request, "Main.html")

def get_recipes(request):
    return render(request, "Content.html")

def get_info_about(request):
    return render(request, "About.html")