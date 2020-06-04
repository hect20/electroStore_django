from django import forms

from tiendaonline.models import Producto,Foto

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

class ProductoDetalle_form(forms.ModelForm):
	class Meta:
		model= Producto
		fields=('titulo','descripcion','precio')
	
		


