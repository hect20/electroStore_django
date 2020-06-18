from django.urls import path
from registro import views
#from tiendaonline import views

urlpatterns = [
    #path('carga_producto/' ,views.producto_view.as_view(), name='carga_producto'),
    #path('registro_cliente/',views.ClienteSignUpView.as_view(), name='registroCliente' ),
    #path('prueba/',views.prueba, name='prueba'),
    #path('login/', views.SignInView.as_view(), name="sign_in"),
    path('registrarse/', views.SignUpView.as_view(), name="registrarse"),
    path('iniciar_sesion/', views.SignInView.as_view(), name="iniciar_sesion"),
    path('cerrar_sesion/', views.SignOutView.as_view(), name='cerrar_sesion'),
   
    path('administrador_alta/<int:id>/', views.AdministradorSignUpView.as_view(), name='administrador_alta'),
    path('administrador_alta', views.AdministradorSignUpView.as_view(), name='administrador_alta'),

]