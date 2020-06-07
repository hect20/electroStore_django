"""electrostore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

#import tiendaonline

#from tiendaonline import views

#agregado#
from tiendaonline.views import index, producto_view #, register, login, logout
from tiendaonline.views import BienvenidaView, SignUpView, SignOutView, SignInView
import tiendaonline
#urlpatterns = [
    #path('', index),
 #   path('admin/', admin.site.urls),
  #  path('producto/', producto_view),



urlpatterns = [
    #path('/', tiendaonline.views.index, name='index'),
    path('admin/', admin.site.urls),
    #path('producto/' ,tiendaonline.views.producto_view, name='producto'),    
    path('', include ('tiendaonline.urls')), #para incluir urls.py de la app

    #path('tiendaonline/', include('tiendaonline.urls')),
]


#Add URL maps to redirect the base URL to our application
# from django.views.generic import RedirectView
# urlpatterns += [
#     path('', RedirectView.as_view(url='/', permanent=True)),
# ]