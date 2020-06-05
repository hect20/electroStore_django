from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
#from django.shortcuts import redirect
from .forms import Productoform, ProductoDetalle_form

#hector
from django.views.generic import ListView,CreateView
from django.db.models import Q
from .models import Producto, Foto



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



#carga de productos
class producto_view(CreateView):
	template_name= 'producto_form.html'
	form_class= Productoform
	success_url= '/producto/'

#lista de todos los productos
class listaProductos(ListView):
	model = Producto
	template_name= 'lista_productos.html'


#buscar un producto
def buscarProducto(request):
	queryset= request.GET.get("buscar")
	productos= Producto.objects.all()
	if queryset:
		productos= Producto.objects.filter(Q(titulo__icontains = queryset)|Q(descripcion__icontains = queryset)).distinct()
	return render(request,'search_results.html',{'productos':productos})

def detalleProducto(request,id):

	producto= get_object_or_404(Producto, pk=id)
	if request.method == "POST":
		formulario= ProductoDetalle_form(request.POST, instance=producto)
		
		if formulario.is_valid():
			producto = formulario.save(commit=False)
			
			producto.save()
			
			return redirect ('home')
	else:
		formulario = ProductoDetalle_form(instance=producto)
	return render(request,'productodetalle.html',{'producto':producto})
	
	
	
	
