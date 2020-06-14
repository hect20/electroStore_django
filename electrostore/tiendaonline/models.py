from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
class Categoria(models.Model):
    nombre= models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    dni= models.PositiveIntegerField()

    def __str__(self):
        return self.dni
    
    objects = models.Manager()

'''     #post_save crea el perfil despues de que un usuario es registrado
    @receiver(post_save, sender=User)
    def crear_usuario_perfil(sender, instance, created, **kwargs):
        if created:
            Usuario.objects.create(user=instance)
    
    @receiver(post_save, sender=User)
    def guardar_usuario_perfil(sender, instance, **kwargs):
        instance.usuario.save()
 '''



class Producto(models.Model):
    titulo= models.CharField(max_length=60)
    descripcion= models.CharField(max_length=3000)
    precio= models.DecimalField(max_digits=7, decimal_places=2)
    promocion= models.PositiveIntegerField(null=False)
    fecha_hora= models.DateField(auto_now=True)
    usuario= models.ManyToManyField(Usuario)
    categoria= models.ForeignKey(Categoria, null=False, blank= False, on_delete= models.CASCADE)
    
    #agregado para evitar advertencia VSC
    objects = models.Manager()
    

class Foto(models.Model):
    nombreArchivo= models.CharField(max_length=40)
    producto= models.ForeignKey(Producto, null=False, blank= False, on_delete= models.CASCADE)
    #agregado
    objects=models.Manager()

    #def __str__(self):
     #   return self.nombreArchivo

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

    def __str__(self):
        return self.nombre