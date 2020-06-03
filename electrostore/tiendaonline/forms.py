from .models import Usuario
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

from tiendaonline.models import Producto


class Productoform(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'titulo',
            'descripcion',
            'precio',
            'promocion',
            'fecha_hora',
            'usuario',
            'categoria',
        ]
        labels = {
            'titulo': 'Nombre',
            'descripcion': 'descripcion',
            'precio': 'precio',
            'promocion': 'promocion',
            'fecha_hora': 'fecha_hora',
            'usuario': 'usuario',
            'categoria': 'categoria',
        }
        widgets = {
			
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
            'promocion': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_hora': forms.DateTimeInput(attrs={'class': 'form-control'}),
			#'fecha_hora': forms.TextInput(attrs={'class': 'form-control'}),
			#self.fields['start_time'].widget = widgets.AdminSplitDateTime()
			'usuario': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }


###########################################################################################
#from django.contrib.auth.models import User


class SignUpForm(forms.ModelForm):
    # (UserCreationForm):
    #    first_name = forms.CharField(max_length=140, required=True)
    #    last_name = forms.CharField(max_length=140, required=False)
    #    email = forms.EmailField(required=True)

    class Meta:
        model = Usuario
        fields = [
            'email',
            'password',
            'nombre',
            'apellido',
			'dni',
		]
        labels = {
            'email': 'Correo',
            'password': 'Password',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'dni': 'DNI',
            
        }



# AGREGADO PARA PRODUCTOS - OMAR
class Productoform2(forms.ModelForm): #ModelForm clase de django que genera el form
    class Meta:
        model = Producto
        fields = ('titulo', 'descripcion')#, 'categoria')

    def __init__(self, *args, **kwargs):
        super(Productoform2, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

