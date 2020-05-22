from django.db import models

# Create your models here.
class Usuario(models.Model):
    email= models.EmailField(max_length=40)
    password= models.CharField(max_length=30)
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=20)
    dni= models.PositiveIntegerField()
    

class Producto(models.Model):
    titulo= models.CharField(max_length=60)
    descripcion= models.CharField(max_length=80)
    precio= models.DecimalField(max_digits=7, decimal_places=2)
    promocion= models.CharField(max_length=60)
    fecha_hora= models.DateField(auto_now=True)
    usuario= models.ManyToManyField(Usuario)

class Categoria(models.Model):
    nombre= models.CharField(max_length=30)

class Foto(models.Model):
    nombreArchivo= models.CharField(max_length=40)

class Compra(models.Model):
    fecha_hora= models.DateField(auto_now=True)
    total= models.DecimalField(max_digits=20, decimal_places=2)
    usuario= models.ForeignKey(Usuario, null=False, blank= False, on_delete= models.CASCADE)

class Itemvendido(models.Model):
    fecha_hora= models.DateField(auto_now=True)
    precio= models.DecimalField(max_digits=20, decimal_places=2)

class Administrador(models.Model):
    email= models.EmailField(max_length=40)
    password= models.CharField(max_length=30)
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=20)
    telefono= models.CharField(max_length=30)

