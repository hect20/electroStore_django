from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre= models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    titulo= models.CharField(max_length=60)
    descripcion= models.CharField(max_length=3000)
    precio= models.DecimalField(max_digits=7, decimal_places=2)
    promocion= models.PositiveIntegerField(null=False)
    fecha_hora= models.DateField(auto_now=True)
    categoria= models.ForeignKey(Categoria, null=False, blank= False, on_delete= models.CASCADE)
    #agregado para evitar advertencia VSC
    objects = models.Manager()

class Usuario(models.Model):
    email= models.EmailField(max_length=50)
    password= models.CharField(max_length=30)
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=20)
    dni= models.PositiveIntegerField()
    producto= models.ManyToManyField(Producto)

    def __str__(self):
        return self.nombre  
    
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
    

