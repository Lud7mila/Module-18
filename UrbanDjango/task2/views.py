from django.shortcuts import render
from django.views import View
#from django.views.generic import TemplateView

def func_index(request):
    return render(request, "func_template.html")

class ClassIndex(View):
    #template_name = "class_template.html"
    def get(self, request):
        return render(request, "class_template.html")

