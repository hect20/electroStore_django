
from django.core.exceptions import PermissionDenied
from django.views import View
from django.contrib.auth.models import User
from .models import Administrador

class GerentePermissionsMixin(object):
    def dispatch(self, request, *args, **kwargs):
        idUser= self.request.user.id
        usuario= User.objects.get(pk= idUser)

        if (usuario.groups.filter(id=2).exists()):
            print ('soy un gerente')
        if not(usuario.groups.filter(id=2).exists()):
            raise PermissionDenied('No tiene acceso!!!!!')
        return super(GerentePermissionsMixin, self).dispatch(request, *args, **kwargs)


class AdminPermissionsMixin(object):
    def dispatch(self, request, *args, **kwargs):
       # model_obj = self.get_object()
        idUser= self.request.user.id
        usuario= User.objects.get(pk= idUser)
        if not(usuario.groups.filter(name='Gerente').exists() or usuario.groups.filter(name='Gestor').exists):
            raise PermissionDenied('No tiene acceso!!!!!')
        return super(AdminPermissionsMixin, self).dispatch(request, *args, **kwargs)
