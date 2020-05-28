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
			'fecha_hora',
			'usuario',
			'categoria',
		]
		labels={
			'titulo': 'Nombre', 
			'descripcion' : 'descripcion',
			'precio': 'precio',
			'promocion': 'promocion',
			'fecha_hora': 'fecha_hora',
			'usuario': 'usuario',
			'categoria': 'categoria',
		}
		widgets={
			'titulo' : forms.TextInput(attrs={'class':'form-control'}),
			'descripcion': forms.TextInput(attrs={'class':'form-control'}),
			'precio': forms.TextInput(attrs={'class':'form-control'}),
			'promocion': forms.TextInput(attrs={'class':'form-control'}),
			'fecha_hora': forms.TextInput(attrs={'class':'form-control'}),
			'usuario': forms.CheckboxSelectMultiple(attrs={'class':'form-control'}),
			'categoria': forms.Select(attrs={'class':'form-control'}),	
		}