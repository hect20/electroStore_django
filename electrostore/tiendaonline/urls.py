from django.conf.urls import url

from . import views
from django.urls import path

urlpatterns = [
    #url(r'^$', views.index, name='index'),

    #url(r'^$', views.BienvenidaView.as_view(), name='bienvenida'),
    path('', views.BienvenidaView.as_view(), name="bienvenida"),

    #url(r'^$', views.producto_view, name='producto'),
    path('', views.producto_view, name="producto"),
    
    #url(r'^registrate/$', views.SignUpView.as_view(), name='sign_up'),
    path('registrate/', views.SignUpView.as_view(), name="sign_up"),
    
    #url(r'^inicia-sesion/$', views.SignInView.as_view(), name='sign_in'),
    path('inicia-sesion/', views.SignInView.as_view(), name="sign_in"),

    #url(r'^cerrar-sesion/$', views.SignOutView.as_view(), name='sign_out'),
    path('cerrar-sesion/', views.SignOutView.as_view(), name="sign_out"),

    #url(r'^producto/$', views.producto_view, name='producto'),
    path('producto/', views.producto_view, name="producto"), #formulario decarga

    #path('iniciar-sesion2/' views.)                                         #seguir aca omar


    ###### agregado ultimo #####

    path('productos/', views.productos, name='productos'),
    path('lista_productos/', views.ProductosView.as_view(), name='lista_productos'),
    path('productos/<int:id>/', views.producto, name='producto'),
    path('lista1/', views.ListadoProductos.as_view(), name='lista1'),

]
