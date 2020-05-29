from django.conf.urls import url

# hector

#fin hector



from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.producto_view, name='producto'),
    
    # hector
     #url(r'^lista$', views.listaProductos.as_view(), name='listaproducto'),
    #fin hector

]
