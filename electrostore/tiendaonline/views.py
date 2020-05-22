from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

def index(request):
    context = {
        'titulo': 'gracias por visitar Electro Store!'
        #'producto': model.producto ej?
    }
    return render(request, 'index.html', context)