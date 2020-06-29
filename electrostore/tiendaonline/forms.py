from django import forms

from tiendaonline.models import Producto,Imagen, Categoria

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
			'descripcion' : 'descripcion',
		}
		widgets={
			'descripcion': forms.Textarea(attrs={'class':'form-control'}),
		}


class ProductoDetalle_form(forms.ModelForm):
	class Meta:
		model= Producto
		fields=('titulo','descripcion','precio', 'promocion')



class EditarProductoForm(forms.ModelForm): #ModelForm clase de django que genera el form
    class Meta:
        model = Producto
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super(EditarProductoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class CategoriaForm(forms.ModelForm): 
	class Meta: 
		model = Categoria 
		fields=[
			'nombre',
		]
		labels={
			'nombre' : 'Nombre',
		}



class ImagenForm(forms.ModelForm): 
	class Meta: 
		model = Imagen 
		fields=[
			'nombreArchivo',
		]
		labels={
			'nombreArchivo' : 'Imagen',
		}