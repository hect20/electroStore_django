from django.urls import path
from tiendaonline import views

urlpatterns = [
    path('',views.index, name='home'),
    path('producto/' ,views.producto_view.as_view(), name='producto'),
    path('lista-producto/',views.listaProductos.as_view(), name='listaproducto'),
    path('buscar/',views.buscarProducto, name='busquedaproducto'),

    ##
    path('materiales/',views.materiales, name='materiales'),
    path('herramientas/',views.herramientas, name='herramientas'),
    path('componentes/',views.componentes, name='componentes'),
    path('kits/',views.kits, name='kits'),

    path('detalle-producto/<int:id>/',views.detalleProducto, name='detalleProducto'),
    

]



