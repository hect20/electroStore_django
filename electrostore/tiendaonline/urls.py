from django.urls import path
from tiendaonline import views

urlpatterns = [
    path('',views.index, name='home'),
    path('carga_producto/' ,views.producto_view.as_view(), name='carga_producto'),
    path('lista-producto/',views.listaProductos.as_view(), name='listaproducto'),
    path('buscar/',views.buscarProducto, name='buscar'),

    ##
    path('materiales/',views.materiales, name='materiales'),
    path('herramientas/',views.herramientas, name='herramientas'),
    path('componentes/',views.componentes, name='componentes'),
    path('kits/',views.kits, name='kits'),

    path('detalle-producto/<int:id>/',views.detalleProducto, name='detalleProducto'),


    path('carro/',views.carrito, name='carro'),
    

]



