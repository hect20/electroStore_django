from django import forms

from tiendaonline.models import Producto

class Productoform(forms.ModelForm): 
	class Meta: 
		model = Producto 
		fields=[
			'titulo', 
			'descripcion',
			'precio',
			'promocion',
			'categoria',
		]
		labels={
			'titulo': 'Nombre', 
			'descripcion' : 'descripcion',
			'precio': 'precio',
			'promocion': 'promocion',			
			'categoria': 'categoria',
		}
		widgets={
			'titulo' : forms.TextInput(attrs={'class':'form-control'}),
			'descripcion': forms.TextInput(attrs={'class':'form-control'}),
			'precio': forms.TextInput(attrs={'class':'form-control'}),
			'promocion': forms.TextInput(attrs={'class':'form-control'}),
			#'fecha_hora': forms.TextInput(attrs={'class':'form-control'}),
			
			'categoria': forms.Select(attrs={'class':'form-control'}),	
		}


#class Busquedaform(form.ModelForm):

