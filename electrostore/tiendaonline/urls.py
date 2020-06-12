from django.urls import path
from tiendaonline import views

urlpatterns = [
    # base
    path('',views.index, name='home'),


    path('categorias/<int:id_pro>',views.mostrar_categoria),
    path('detalle-producto/<int:id>/',views.detalleProducto, name='detalleProducto'),
    #
    
    path('base/',views.base.as_view(), name='base'),


    
    path('carga_producto/' ,views.producto_view.as_view(), name='carga_producto'),
    path('lista_productos/',views.listaProductos.as_view(), name='listaproductos'),
    path('buscar/',views.buscarProducto, name='buscar'),

    ##
   
    #########
    
   
    
    #########
  


    path('carro/',views.carrito, name='carro'),
    
    # omar - editar producto
    path('lista_productos/eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
    path('lista_productos/<int:id>/', views.editar_producto, name='editar_producto'),
]



