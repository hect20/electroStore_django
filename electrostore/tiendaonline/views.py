from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from .forms import Productoform

#hector
from django.views.generic import ListView,CreateView
from django.db.models import Q
from .models import Producto



# Create your views here.

def materiales(request):
	return render(request,"materiales.html")

def herramientas(request):
	return render(request,"herramientas.html")

def componentes(request):
	return render(request,"componentes.html")

def kits(request):
	return render(request,"kits.html")





def index(request):
    context = {
        'titulo': 'gracias por visitar Electro Store!'
        #'producto': model.producto ej?
    }
    return render(request, 'index.html', context)


###########################################

class producto_view(CreateView):
	template_name= 'producto_form.html'
	form_class= Productoform
	success_url= '/producto/'

###########################################3
class listaProductos(ListView):
	model = Producto
	template_name= 'lista_productos.html'



def buscarProducto(request):
	queryset= request.GET.get("buscar")
	productos= Producto.objects.all()
	if queryset:
		productos= Producto.objects.filter(Q(titulo__icontains = queryset)).distinct()
	return render(request,'search_results.html',{'productos':productos})



