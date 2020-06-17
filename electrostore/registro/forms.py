from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from tiendaonline.models import Usuario
from django import forms

class SignUpForm(UserCreationForm):
    #first_name = forms.CharField(max_length=140, required=True)
    #last_name = forms.CharField(max_length=140, required=False)
    #email = forms.EmailField(required=True)
    #dni = forms.IntegerField()
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
