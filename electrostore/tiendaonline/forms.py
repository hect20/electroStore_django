from django import forms

from tiendaonline.models import Producto,Foto

class Productoform(forms.ModelForm): 
	class Meta: 
		model = Producto 
		fields=[
			'categoria',
			'titulo', 
			'descripcion',
			'precio',
			'promocion',
			
		]
		labels={
			'descripcion' : 'descripcion'
		}
		widgets={
			'descripcion': forms.Textarea(attrs={'class':'form-control'}),
		}


class ProductoDetalle_form(forms.ModelForm):
	class Meta:
		model= Producto
		fields=('titulo','descripcion','precio', 'promocion')
