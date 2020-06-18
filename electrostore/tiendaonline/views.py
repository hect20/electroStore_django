from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, HttpResponseRedirect
#from django.shortcuts import redirect
from .forms import Productoform, ProductoDetalle_form, EditarProductoForm, CategoriaForm

# hector
from django.views.generic import ListView, CreateView
from django.db.models import Q
from .models import Producto, Foto, Categoria


# Create your views here.

class materiales(ListView):
    model = Producto
    template_name = 'materiales.html'
    context_object_name = 'tipoMaterial'

    def get_queryset(self):
        return Producto.objects.filter(categoria__nombre='Materiales')


class herramientas(ListView):
    model = Producto
    template_name = 'herramientas.html'
    context_object_name = 'tipoHerramientas'

    def get_queryset(self):
        return Producto.objects.filter(categoria__nombre='Herramientas')


class componentes(ListView):
    model = Producto
    template_name = 'componentes.html'
    context_object_name = 'tipoComponentes'

    def get_queryset(self):
        return Producto.objects.filter(categoria__nombre='Componentes')


class kits(ListView):
    model = Producto
    template_name = 'kits.html'
    context_object_name = 'tipoKits'
    def get_queryset(self):
        return Producto.objects.filter(categoria__nombre='kits de arduino')



def index(request):
    context = {
        'titulo': 'gracias por visitar Electro Store!'
        # 'producto': model.producto ej?
    }
    return render(request, 'index.html', context)


class producto_promocion(ListView):
    model = Producto
    template_name = 'index.html'
    context_object_name = 'producto_promocion'

    def get_queryset(self):
        return Producto.objects.filter(promocion__gt=0)[0:8]

# carga de productos


class ProductoAlta(CreateView):
    template_name = 'producto_alta.html'
    form_class = Productoform
    success_url = '/lista_productos/'


# lista de todos los productos
class listaProductos(ListView):
    model = Producto
    template_name = 'lista_productos.html'

# buscar un producto


def buscarProducto(request):
    queryset = request.GET.get("buscar")
    productos = Producto.objects.all()
    if queryset:
        productos = Producto.objects.filter(Q(titulo__icontains=queryset) | Q(
            descripcion__icontains=queryset)).distinct()
    return render(request, 'search_results.html', {'productos': productos})


def detalleProducto(request, id):
    imagenes = Foto.objects.filter(producto=id)
    producto = get_object_or_404(Producto, pk=id)

    precioFinal = producto.precio - \
        ((producto.precio * producto.promocion) / 100)
    descuento = producto.precio != precioFinal  # boolean para prueba

    if request.method == "POST":
        formulario = ProductoDetalle_form(request.POST, instance=producto)

        if formulario.is_valid():
            producto = formulario.save(commit=False)

            producto.save()

            return redirect('home')
    else:
        formulario = ProductoDetalle_form(instance=producto)
    return render(request, 'productodetalle.html', {'producto': producto, 'imagenes': imagenes, 'precioFinal': precioFinal, 'descuento': descuento})


def carrito(request):
    return render(request, 'carrito.html')


# omar - editar producto
def editar_producto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    if request.method == "POST":
        formulario = Productoform(request.POST, instance=producto)
        if formulario.is_valid():
            producto = formulario.save(commit=False)
            producto.save()
            return redirect('lista_productos')
    else:
        formulario = Productoform(instance=producto)
    return render(request, 'editar_producto.html', {'producto': formulario})


def eliminar_producto(request, id):
    Producto.objects.filter(pk=id).delete()
    return redirect('lista_productos')



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