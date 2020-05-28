from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index')
    url(r'^$', view.producto_view, name='producto')
    
]
