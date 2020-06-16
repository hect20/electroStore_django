from django.urls import path
from tiendaonline import views

urlpatterns = [
   
    path('',views.index, name='home'),


    path('categorias/<int:id_pro>',views.mostrar_categoria),
    path('detalle-producto/<int:id>/',views.detalleProducto, name='detalleProducto'),
    #path('carga_imagen/<int:id>' ,views.imagen_producto.as_view(), name='imagen_producto'),

    path('lista_productos/',views.listaProductos.as_view(), name='listaproductos'),
    path('buscar/',views.buscarProducto, name='buscar'),
    
    path('search/',views.SearchResultsView.as_view(), name ='search_results'),
     
    # Agregado hector
    #path('buscar/',views.buscar_producto.as_view(), name='buscar'),

    #path('buscar2/',views.buscar_producto2.as_view(), name='search_results2'),

    #
    path('carga_producto/' ,views.carga_producto.as_view(), name='carga_producto'),
    path('lista_productos/<int:pk>/', views.editar_producto.as_view(), name='editar_producto'),
    path('lista_productos/eliminar/<int:pk>/', views.eliminar_producto.as_view(), name='eliminar_producto'),

]



