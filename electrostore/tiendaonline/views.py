from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'titulo': 'gracias por visitar Electro Store!'
        #'producto': model.producto ej?
    }
    return render(request, 'index.html', context)



def categ_prod (request):
    return render (request,"categoria_producto.html")