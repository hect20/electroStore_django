from django.urls import path
from tiendaonline import views

urlpatterns = [
    #path('',views.index, name='home'),

    path('carga_producto/' ,views.producto_view.as_view(), name='carga_producto'),
    path('lista_productos/',views.listaProductos.as_view(), name='listaproductos'),
    path('buscar/',views.buscarProducto, name='buscar'),

    ##
    path('materiales/',views.materiales.as_view(), name='materiales'),
    path('herramientas/',views.herramientas.as_view(), name='herramientas'),
    path('componentes/',views.componentes.as_view(), name='componentes'),
    path('kits/',views.kits.as_view(), name='kits'),

    #########
    path('',views.index, name='home'),
    path('categorias/',views.categorias.as_view(),name='categorias'),
    path('categorias/<int:id_pro>',views.mostrar_categoria,name='categorias2'),
    
    #########
    path('detalle-producto/<int:id>/',views.detalleProducto, name='detalleProducto'),


    path('carro/',views.carrito, name='carro'),
    
    # omar - editar producto
    path('lista_productos/eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
    path('lista_productos/<int:id>/', views.editar_producto, name='editar_producto'),
]



