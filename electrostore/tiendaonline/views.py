from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, HttpResponseRedirect
#from django.shortcuts import redirect
from .forms import  ProductoDetalle_form, EditarProductoForm, CategoriaForm,Productoform

# hector
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView,TemplateView
from django.db.models import Q
from .models import Producto, Imagen, Categoria, Administrador, Usuario, User
#omar - para restringir accesos
from django.contrib.auth.decorators import login_required

from django.contrib.auth import models
from .mixins import AdminPermissionsMixin, GerentePermissionsMixin
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.










# View para Filtrar los componentes del index: Promocion y Los mas Likeados
class producto_promocion(ListView):
    model = Producto
    template_name = 'index.html'
    context_object_name = 'producto_promocion'

    def get_queryset(self):
        return Producto.objects.filter(promocion__gt=0)[0:8]
## Fin View Index



# Barra Dinamica de Categorias
class MostrarCategoria(ListView):
	model= Producto
	template_name= 'categoria.html'
	context_object_name='productoss'
	def get_queryset(self):
		return Producto.objects.filter(categoria=self.kwargs['pk'])
# Fin Barra Dinamica


# Detalle de un Producto, Precio Final, Descuento
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
## Fin Detalle


# Lista de Todos los Productos
class ListaProductos(AdminPermissionsMixin, ListView): #LoginRequiredMixin
    model = Producto
    template_name = 'lista_productos.html'
    paginate_by= 8
## Fin Lista

# Buscar un Producto
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
## Fin Busqueda

class Carrito(TemplateView):
    template_name='carrito.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articulos'] = 'hola'
        return context

############################## Administradores######################################

# Cargar Producto
class ProductoAlta(CreateView):
    model= Producto
    template_name = 'producto_alta.html'
    fields= ('categoria','titulo','precio','promocion','descripcion')
    #form_class = Productoform
    success_url = '/lista_productos/'

# Editar un Producto
class ProductoModificar(UpdateView):
    model= Producto
    fields= ('categoria','titulo','precio','promocion','descripcion')
    #form_class= EditarProductoForm
    template_name= 'editar_producto.html'
    success_url= '/lista_productos/'

# Eliminar un Producto
class ProductoBaja(DeleteView):
	model= Producto
	context_object_name= 'producto'
	template_name= 'eliminar_producto.html'
	success_url= '/lista_productos/'
## Fin Eliminar



# Lista de Categorias
class CategoriaLista(LoginRequiredMixin, ListView):
    model = Categoria
    template_name = 'categoria_lista.html'
    paginate_by= 3

## Fin Lista de Categorias


# Cargar Categoria
class CategoriaAlta(CreateView):
    template_name = 'categoria_alta.html'
    form_class = CategoriaForm
    success_url = '/categoria_lista/'
##



class CategoriaModificar(UpdateView):
    model= Categoria
    #fields= ('categoria','titulo','precio','promocion','descripcion')
    form_class= CategoriaForm
    context_object_name= 'categoria'
    template_name= 'categoria_modificar.html'
    
    success_url= '/categoria_lista/'



class CategoriaBaja(DeleteView):
	model= Categoria
	context_object_name= 'categoria'
	template_name= 'eliminar_categoria.html'
	success_url= '/categoria_lista/'



class ImagenCarga(CreateView):
    model= Imagen
    template_name= 'imagen_carga.html'
    fields= '__all__'
    success_url = '/lista_productos/'






