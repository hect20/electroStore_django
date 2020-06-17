from django.shortcuts import render, redirect
from tiendaonline.models import Usuario
from django.contrib.auth.models import User, Group
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext #para enviar var al template?
from registro.forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView

class SignUpView(CreateView):                           #registrarse
    model= Usuario
    form_class= SignUpForm
    template_name= 'registro/registrar.html'

    def form_valid(self, form):
        user= form.save()                                     #Si es valido lo guarda
        
        group = Group.objects.get(name='Usuario')
        user.groups.add(group)
        
        usuario= form.cleaned_data.get('username')      #obtiene datos del form para mostrarlos
        password= form.cleaned_data.get('password1')   
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/')
    

class SignInView(LoginView):                            #iniciar sesion
    template_name = 'registro/iniciar_sesion.html'

class SignOutView(LogoutView):                          #cerrar sesion
    pass
