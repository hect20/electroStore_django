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
		
#class Busquedaform(form.ModelForm):

