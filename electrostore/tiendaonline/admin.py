from django.contrib import admin
from .models import Categoria, Usuario, Producto, Foto, Compra, Itemvendido, Administrador

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(Foto)
admin.site.register(Compra)
admin.site.register(Itemvendido)
admin.site.register(Administrador)
