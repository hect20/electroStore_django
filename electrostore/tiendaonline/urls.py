from django.conf.urls import url
from django.urls import path, re_path
from . import views

#app_name="tiendaonline_app"

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
