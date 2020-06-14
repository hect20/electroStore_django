from django.urls import path
from tiendaonline import views

urlpatterns = [
    # base
    path('',views.index, name='home'),


    path('categorias/<int:id_pro>',views.mostrar_categoria),
    path('detalle-producto/<int:id>/',views.detalleProducto, name='detalleProducto'),
    #

    path('carga_producto/' ,views.producto_view.as_view(), name='carga_producto'),

  #  path('carga_imagen/<int:id>' ,views.imagen_producto.as_view(), name='imagen_producto'),

    path('lista_productos/',views.listaProductos.as_view(), name='listaproductos'),
    path('buscar/',views.buscarProducto, name='buscar'),

    ##
   
    #########
    
    #########
  
    # omar - editar producto
    #path('lista_productos/eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),

    path('lista_productos/<int:pk>/', views.editar_producto.as_view(), name='editar_producto'),

    path('lista_productos/<int:pk>/', views.eliminar_producto.as_view(), name='eliminar_producto'),

]



