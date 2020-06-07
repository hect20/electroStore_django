from django.shortcuts import render, redirect

from .forms import Productoform

# Create your views here.

def index(request):
    context = {
        'titulo': 'gracias por visitar Electro Store!'
    }
    return render(request, 'index.html', context)

def producto_view(request): 
	if request.method == 'POST': 
	  	form = Productoform(request.POST)
	  	if form.is_valid():
	  		form.save()
	  	return redirect('/')
	else: 
		form = Productoform(request.POST)

	return render(request, 'producto_form.html',{'form': form})



##########################################################################
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView
from .models import Usuario

from .forms import SignUpForm


class SignUpView(CreateView):
    model = Usuario
    form_class = SignUpForm

    def form_valid(self, form):
        '''
        En este parte, si el formulario es valido guardamos lo que se obtiene de él y usamos authenticate 
		para que el usuario incie sesión luego de haberse registrado y lo redirigimos al index
        '''
        form.save()
        usuario = form.cleaned_data.get('usuario')	# OMAR -FUNCIONA CUANDO HAGA EL LOGIN
        password = form.cleaned_data.get('password')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/')

class BienvenidaView(TemplateView):
   template_name = 'bienvenida.html'




class SignInView(LoginView):
    template_name = 'iniciar_sesion.html'


from django.contrib.auth.views import LoginView, LogoutView 

class SignOutView(LogoutView):
    pass


###################################################################
""" from django.contrib import auth                     ##PARA LOGIN NUEVO
from django.http import HttpResponseRedirect

class LoginUsuario():
    model = Usuario
    username
    password
    def login(request):
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect("/bienvenida/")
        else:
            # Show an error page
            return HttpResponseRedirect("/account/invalid/") """
######################################################################
from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Categoria # ver tema categoria
from .forms import Productoform2
#from tiendaonline.models import Producto

#PARA EL PUNTO 5 PENDIENTE: un submenu con todas las categorias, hacer click para filtrar la lista
#o hacerlo con un buscador (mas dificil?)
#o boton para ordenar en cada campo

#NO poner logica(orden) en el template

#ver order_by para ordenar/ no necesario
#devuelve todos los obj de la clase Producto
from django.views import generic
from tiendaonline.models import Producto, Categoria

class ProductosView(generic.ListView):
    model = Producto
    paginate_by = 20
    template_name = 'productos1.html'


class ListadoProductos(TemplateView):
    template_name = 'productos1.html'
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['productos']=Producto.objects.all()
        return context


def productos(request): 
    prod = Producto.objects.all()
    return render(request, 'productos.html', {'prod': prod})

def producto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    if request.method == "POST":
        formulario = Productoform2(request.POST, instance=producto)
        if formulario.is_valid():
            producto = formulario.save(commit = False)
            producto.save()
            return redirect('productos')
    else:
        formulario = Productoform2 (instance= producto)
    return render(request, 'producto.html', {'producto': formulario})



def eliminarProducto(request, id):
    Producto.objects.filter(pk=id).delete()
    return redirect(productos)