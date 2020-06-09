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
			'descripcion' : 'descripcion',
		}
		widgets={
			'descripcion': forms.Textarea(attrs={'class':'form-control'}),
		}


class ProductoDetalle_form(forms.ModelForm):
	class Meta:
		model= Producto
		fields=('titulo','descripcion','precio', 'promocion')



#omar editar producto
class EditarProductoForm(forms.ModelForm): #ModelForm clase de django que genera el form
    class Meta:
        model = Producto
        fields = ('titulo', 'descripcion')#, 'categoria')

    def __init__(self, *args, **kwargs):
        super(EditarProductoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

