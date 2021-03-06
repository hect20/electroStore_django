from django.urls import path
from tiendaonline import views


urlpatterns = [
    path('',views.index.as_view(), name='home'),

    #path('prueba/',views.Prueba_crispy.as_view(), name='prueba'),
    ##
    path('categorias/<int:pk>',views.MostrarCategoria.as_view(), name='categorias'),
    path('producto_detalle/<int:pk>/',views.ProductoDetalle.as_view(), name='producto_detalle'),


    path('lista_productos/',views.ListaProductos.as_view(), name='lista_productos'),
    #path('producto_alta/' ,views.ProductoAlta.as_view(), name='producto_alta'),

    path('producto_alta/',views.ProductoAlta, name='producto_alta'),

    path('lista_productos/<int:pk>/', views.ProductoModificar.as_view(), name='editar_producto'),
    path('lista_productos/eliminar/<int:pk>/', views.ProductoBaja.as_view(), name='eliminar_producto'),

    path('lista_productos/imagen/<int:pk>/', views.ImagenCarga.as_view(), name='carga_imagen_producto'),

    path('buscar/',views.BuscarProducto.as_view(), name='buscar'),
    
    


    path('categoria_lista/',views.CategoriaLista.as_view(), name='categoria_lista'),
    path('categoria_alta/' ,views.CategoriaAlta.as_view(), name='categoria_alta'),
    path('categoria_lista/<int:pk>/', views.CategoriaModificar.as_view(), name='categoria_modificar'),
    path('categoria_lista/eliminar/<int:pk>/', views.CategoriaBaja.as_view(), name='categoria_baja'),


    path('producto_alta/<int:pk>/', views.ImagenCarga.as_view(), name='imagen_carga'),

    
    #path('carrito/<int:pk>',views.Carrito.as_view(), name='carrito'),

    

]



