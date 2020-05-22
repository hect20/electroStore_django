import json

from random import randrange
from tiendaonline.models import Usuario

with open('USUARIOS.json', 'r') as fp:
    usuarios = json.load(fp)

for a in usuarios:
    n = Usuario(email=a['email'], password=a['password'], nombre=a['nombre'], apellido=a['apellido'], dni=a['dni'])
    n.save()
    print('GUARDANDO USUARIO...')