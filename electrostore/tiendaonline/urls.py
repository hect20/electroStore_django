from django.urls import path
from tiendaonline import views


urlpatterns = [
    path('',views.producto_promocion.as_view(), name='home'),
    ###

    #path('prueba/',views.Prueba_crispy.as_view(), name='prueba'),
    ##
    path('categorias/<int:pk>',views.MostrarCategoria.as_view(), name='categorias'),
    path('producto_detalle/<int:pk>/',views.ProductoDetalle.as_view(), name='producto_detalle'),
    ##

    ##
    path('lista_productos/',views.listaProductos.as_view(), name='lista_productos'),
    path('producto_alta/' ,views.ProductoAlta.as_view(), name='producto_alta'),
    path('lista_productos/<int:pk>/', views.editar_producto.as_view(), name='editar_producto'),
    path('lista_productos/eliminar/<int:pk>/', views.eliminar_producto.as_view(), name='eliminar_producto'),

   
    #path('detalle-producto/<int:id>/',views.detalleProducto, name='detalleProducto'),
    
    ##

    path('buscar/',views.BuscarProducto.as_view(), name='buscar'),
    
    ##
    
    ##
    path('carro/',views.carrito, name='carro'),
    ##
    path('categoria_alta/' ,views.CategoriaAlta.as_view(), name='categoria_alta'),
    path('categoria_lista/',views.CategoriaLista.as_view(), name='categoria_lista'),


    path('categoria_lista/eliminar/<int:pk>/', views.CategoriaBaja.as_view(), name='categoria_baja'),

    path('categoria_lista/<int:pk>/', views.CategoriaModificar.as_view(), name='categoria_modificar'),

]



