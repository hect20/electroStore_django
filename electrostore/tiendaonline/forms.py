from django import forms

from tiendaonline.models import Producto,Foto, Categoria


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


class CategoriaForm(forms.ModelForm): 
	class Meta: 
		model = Categoria 
		fields=[
			'nombre',
		]
		labels={
			'nombre' : 'Nombre',
		}
