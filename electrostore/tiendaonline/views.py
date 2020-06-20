from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, HttpResponseRedirect
#from django.shortcuts import redirect
from .forms import  ProductoDetalle_form, EditarProductoForm, CategoriaForm,Productoform

# hector
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q
from .models import Producto, Foto, Categoria


# Create your views here.

def index(request):
    context = {
        'titulo': 'gracias por visitar Electro Store!'
        # 'producto': model.producto ej?
    }
    return render(request, 'index.html', context)

class MostrarCategoria(ListView):
	model= Producto
	template_name= 'categoria.html'
	context_object_name='productoss'
	def get_queryset(self):
		return Producto.objects.filter(categoria=self.kwargs['pk'])

class ProductoDetalle(DetailView):
	model= Producto
	template_name= 'producto_detalle.html'
	context_object_name= 'producto'
	def get_context_data(self,**kwargs):
		context= super().get_context_data(**kwargs)
		producto= self.object
		precioFinal= producto.precio - ((producto.precio * producto.promocion) / 100)
		descuento= producto.precio != precioFinal

		context['precioFinal']= precioFinal
		context['descuento']= descuento
		return context

class producto_promocion(ListView):
    model = Producto
    template_name = 'index.html'
    context_object_name = 'producto_promocion'

    def get_queryset(self):
        return Producto.objects.filter(promocion__gt=0)[0:8]

# carga de productos

######
class Prueba_crispy(CreateView):
    model= Producto
    template_name= 'prueba_crispy.html'
    fields= ('categoria','titulo','precio','promocion','descripcion')
    success_url = '/lista_productos/'
######





# lista de todos los productos
class listaProductos(ListView):
    model = Producto
    template_name = 'lista_productos.html'

# buscar un producto

class BuscarProducto (ListView):
	model  = Producto
	template_name  =  'search_results.html'
	context_object_name= 'productos'
	def get_queryset(self):
		query= self.request.GET.get("buscado")
		
		object_list= Producto.objects.all()
		if query:
			object_list= Producto.objects.filter(Q(titulo__icontains = query)|Q(descripcion__icontains = query)).distinct()
		return object_list


def carrito(request):
    return render(request, 'carrito.html')


####hector
class ProductoAlta(CreateView):
    model= Producto
    template_name = 'producto_alta.html'
    fields= ('categoria','titulo','precio','promocion','descripcion')
    #form_class = Productoform
    success_url = '/lista_productos/'

# Editar un Producto
class editar_producto(UpdateView):
    model= Producto
    fields= ('categoria','titulo','precio','promocion','descripcion')
    #form_class= EditarProductoForm
    template_name= 'editar_producto.html'
    success_url= '/lista_productos/'

# Eliminar un Producto
class eliminar_producto(DeleteView):
	model= Producto
	context_object_name= 'producto'
	template_name= 'eliminar_producto.html'
	success_url= '/lista_productos/'

#finHector



#########################
class CategoriaAlta(CreateView):
    template_name = 'categoria_alta.html'
    form_class = CategoriaForm
    success_url = '/categoria_lista/'


class CategoriaLista(ListView):
    model = Categoria
    template_name = 'categoria_lista.html'

    #context_object_name= 'listaCategorias'
    #def get_context_data(self, **kwargs):
        #context= super().get_context_data(**kwargs)
        
        #categoriasEnProducto= Producto.objects.filter(categoria__id__isnull=False)
        #categorias= Categoria.objects.all()
        #categorias.objects.filter
        
        #context['categoriasEnProducto']= categoriasEnProducto
        #return context



def categoriaModificar(request, id):
    categoria = get_object_or_404(Categoria, pk=id)
    if request.method == "POST":
        formulario = CategoriaForm(request.POST, instance=categoria)
        if formulario.is_valid():
            categoria = formulario.save(commit=False)
            categoria.save()
            return redirect('categoria_lista')
    else:
        formulario = CategoriaForm(instance=categoria)
    return render(request, 'categoria_modificar.html', {'categoria': formulario})



def categoriaBaja(request, id):
    Categoria.objects.filter(pk=id).delete()
    return redirect('categoria_lista')