from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib import messages
#from django.shortcuts import redirect
from .forms import  ProductoDetalle_form, EditarProductoForm, CategoriaForm, ImagenForm, ProductoFormPrueba, ImagenFormPrueba

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView,TemplateView
from django.db.models import Q
from .models import Producto, Imagen, Categoria

from django.forms import modelformset_factory
# Create your views here.


def index(request):
    all_items = Producto.objects.filter(promocion__gt=0)[0:9]
    pics = []
    for a in all_items:
        images = Imagen.objects.filter(producto=a.pk)
        pics.append(images)
    #propert = Item.objects.filter(active=True)
    context = {
        'imagenes': pics,
        'producto_promocion':all_items,
    }

    return render(request, 'index.html', context)




# View para Filtrar los componentes del index: Promocion y Los mas Likeados
""" class index(ListView):
    model= Producto
    template_name= 'index.html'
    context_object_name= 'producto'
    def get_context_data(self,**kwargs):
        context= super().get_context_data(**kwargs)
        productos= Producto.objects.filter(promocion__gt=0)[0:9]
        #producto_promocion= Imagen.objects.filter(producto__id=producto)
        imagenes= Imagen.objects.all()
        #ofertas= productos.object.filter()
        context['producto_promocion']= productos
        context['imagenes']=imagenes

        return context """



""" class producto_promocion(ListView):
    model = Producto
    template_name = 'index.html'
    context_object_name = 'producto_promocion'

    def get_queryset(self):
        return Producto.objects.filter(promocion__gt=0)[0:8]
## Fin View Index """



# Barra Dinamica de Categorias
class MostrarCategoria(ListView):
	model= Producto
	template_name= 'categoria.html'
	context_object_name='productoss'
	def get_queryset(self):
		return Producto.objects.filter(categoria=self.kwargs['pk'])
# Fin Barra Dinamica


class ProductoDetalle(DetailView):
    model= Producto
    template_name= 'producto_detalle.html'
    context_object_name= 'producto'

    def get_context_data(self,**kwargs):
        context= super().get_context_data(**kwargs)
        producto= self.object
        precioFinal= producto.precio - ((producto.precio*producto.promocion)/100)
        descuento= producto.precio != precioFinal
        context['imagenes']= Imagen.objects.filter(producto=self.kwargs['pk'])
        context['precioFinal']=precioFinal
        context['descuento']=descuento
        return context

# Detalle de un Producto, Precio Final, Descuento



# Lista de Todos los Productos
class ListaProductos(ListView):
    model = Producto
    template_name = 'lista_productos.html'
    paginate_by = 8
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

""" class Carrito(TemplateView):
    template_name='carrito.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articulos'] = 'hola'
        return context """

############################## Administradores######################################

# Cargar Producto
""" class ProductoAlta(CreateView):
    model= Producto
    template_name = 'producto_alta.html'
    fields= ('categoria','titulo','precio','promocion','descripcion')
    #form_class = Productoform
    success_url = '/lista_productos/' """

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
class CategoriaLista(ListView):
    model = Categoria
    template_name = 'categoria_lista.html'

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
    #form_class = ImagenForm
    success_url = '/lista_productos/'



def ProductoAlta(request):
    ImagenFormSet= modelformset_factory(Imagen,form=ImagenFormPrueba,extra=3)
    if request.method == 'POST':
        productoForm= ProductoFormPrueba(request.POST)
        formset= ImagenFormSet(request.POST, request.FILES, queryset=Imagen.objects.none())
        if productoForm.is_valid() and formset.is_valid():
            producto_form= productoForm.save(commit=False)
            
            producto_form.save()
           
            for form in formset.cleaned_data:
                try:
                    imagen= form['nombreArchivo']
                    foto= Imagen(producto=producto_form,nombreArchivo=imagen)
                    foto.save()
                except Exception as e:
                    break
            return HttpResponseRedirect("/lista_productos/")
        else:
            print ('productoForm.errors, formset.errors')
    else:
        productoForm= ProductoFormPrueba()
        formset= ImagenFormSet(queryset= Imagen.objects.none())
    return render(request,'producto_alta.html',{'productoForm':productoForm,'formset':formset})

