from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from tiendaonline.models import Usuario, Administrador
from django import forms

class SignUpForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
            'dni'
        )

class AdministradorSignUpForm(UserCreationForm):
    class Meta:
        model = Administrador
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
            'telefono',
            'cargo',
        )