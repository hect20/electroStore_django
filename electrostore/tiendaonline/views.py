from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, HttpResponseRedirect
#from django.shortcuts import redirect
from .forms import Productoform, ProductoDetalle_form, EditarProductoForm

#hector
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Producto, Foto, Categoria


#class imagen_producto (CreateView):
#	model= Foto
#	fields= ['nombreArchivo','producto']
#	def carga(self, id_producto):


def index(request):
	return render(request,'index.html')


def mostrar_categoria(request,id_pro):
	productoss=Producto.objects.filter(categoria=id_pro)
	return render(request,'categoria.html',{'productoss':productoss})
#########


def detalleProducto(request,id):
	imagenes= Foto.objects.filter(producto=id)
	producto= get_object_or_404(Producto, pk=id)

	precioFinal= producto.precio - ((producto.precio * producto.promocion) / 100)
	descuento= producto.precio != precioFinal #boolean para prueba

	if request.method == "POST":
		formulario= ProductoDetalle_form(request.POST, instance=producto)
		
		if formulario.is_valid():
			producto = formulario.save(commit=False)
			
			producto.save()
			
			return redirect ('home')
	else:
		formulario = ProductoDetalle_form(instance=producto)
	return render(request,'productodetalle.html',{'producto':producto,'imagenes':imagenes, 'precioFinal': precioFinal, 'descuento': descuento})





#lista de todos los productos con sus caracteristicas
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








# Gerente, Administrador

# Carga de Productos
class carga_producto(CreateView):
	template_name= 'carga_producto.html'
	form_class= Productoform
	success_url= '/lista_productos/'

# Editar un Producto
class editar_producto(UpdateView):
	model= Producto
	form_class= EditarProductoForm
	template_name= 'editar_producto.html'
	success_url= '/lista_productos/'
	
# Eliminar un Producto
class eliminar_producto(DeleteView):
	model= Producto
	context_object_name= 'producto'
	template_name= 'eliminar_producto.html'
	success_url= '/lista_productos/'

#def eliminar_producto(request, id):
#	Producto.objects.filter(pk=id).delete()
#	return redirect ('listaproductos')