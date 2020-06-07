from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
#from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nombre= models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    email= models.EmailField(max_length=50)
    password= models.CharField(max_length=30)
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=20)
    dni= models.PositiveIntegerField()

    def __str__(self):
        return self.nombre

    #@receiver(post_save)
def crear_usuario_perfil(instance, created, **kwargs):
    if created:
        Usuario.objects.create(Usuario= instance)

    #@receiver(post_save)
def guardar_usuario_perfil(instance, **kwargs):
    instance.perfil.save()

class Producto(models.Model):
    titulo= models.CharField(max_length=60)
    descripcion= models.CharField(max_length=80)
    precio= models.DecimalField(max_digits=7, decimal_places=2)
    promocion= models.CharField(max_length=60)
    fecha_hora= models.DateField()
    usuario= models.ManyToManyField(Usuario)
    categoria= models.ForeignKey(Categoria, null=False, blank= False, on_delete= models.CASCADE)
    
    objects= models.Manager()

    def __str__(self):
            return self.titulo
        

class Foto(models.Model):
    nombreArchivo= models.CharField(max_length=40)
    producto= models.ForeignKey(Producto, null=False, blank= False, on_delete= models.CASCADE)

class Compra(models.Model):
    fecha_hora= models.DateField(auto_now=True)
    total= models.DecimalField(max_digits=20, decimal_places=2)
    usuario= models.ForeignKey(Usuario, null=False, blank= False, on_delete= models.CASCADE)

class Itemvendido(models.Model):
    fecha_hora= models.DateField(auto_now=True)
    precio= models.DecimalField(max_digits=20, decimal_places=2)
    compra= models.ForeignKey(Compra,null=False, blank= False, on_delete= models.CASCADE)
    producto= models.ForeignKey(Producto, null=False, blank= False, on_delete= models.CASCADE)

class Administrador(models.Model):
    email= models.EmailField(max_length=40)
    password= models.CharField(max_length=30)
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=20)
    telefono= models.CharField(max_length=30)

