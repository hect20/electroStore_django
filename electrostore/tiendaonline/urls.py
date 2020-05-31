from django.urls import path
from tiendaonline import views

urlpatterns = [
    path('',views.index, name='home'),
    path('producto/' ,views.producto_view, name='producto'),
    path('lista-producto/',views.listaProductos.as_view(), name='listaproducto'),
]


