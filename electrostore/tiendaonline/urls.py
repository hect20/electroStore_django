from django.urls import path
from tiendaonline import views


urlpatterns = [
    path('',views.producto_promocion.as_view(), name='home'),

    ##
    path('categorias/<int:pk>',views.mostrar_categoria.as_view(), name='categorias'),
    path('producto_detalle/<int:pk>/',views.ProductoDetalle.as_view(), name='producto_detalle'),
    ##

    ##
    path('producto_alta/' ,views.ProductoAlta.as_view(), name='producto_alta'),
    path('lista_productos/',views.listaProductos.as_view(), name='lista_productos'),
    path('lista_productos/eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
    path('lista_productos/<int:id>/', views.editar_producto, name='editar_producto'),
    #path('detalle-producto/<int:id>/',views.detalleProducto, name='detalleProducto'),
    
    ##

    path('buscar/',views.buscar_producto.as_view(), name='buscar'),
    
    ##
    
    ##
    path('carro/',views.carrito, name='carro'),
    ##
    path('categoria_alta/' ,views.CategoriaAlta.as_view(), name='categoria_alta'),
    path('categoria_lista/',views.CategoriaLista.as_view(), name='categoria_lista'),
    path('categoria_lista/eliminar/<int:id>/', views.categoriaBaja, name='categoria_baja'),
    path('categoria_lista/<int:id>/', views.categoriaModificar, name='categoria_modificar'),

]



