from django.shortcuts import render

from django.shortcuts import redirect

from .forms import Productoform

#hector
from tiendaonline.models import Producto
from django.views.generic import ListView


# Create your views here.

def index(request):
    context = {
        'titulo': 'gracias por visitar Electro Store!'
        #'producto': model.producto ej?
    }
    return render(request, 'index.html', context)

def producto_view(request): 
	  if request.method == 'POST': 
	  	form = Productoform(request.POST)
	  	if form.is_valid():
	  		form.save()
	  	return redirect('producto')
	  else: 
	  	form = Productoform(request.POST)
	  return render(request, 'producto_form.html',{'form': form}) 

class listaProductos(ListView):
	model = Producto
	template_name= 'lista_productos.html'









##