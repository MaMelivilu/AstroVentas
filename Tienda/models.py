from django.db import models

# Create your models here.
class Categoria(models.Model):
    categoria_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        txt = "Nombre: {0} - {1}"
        return txt.format(self.nombre,self.categoria_id)

#registro de piezas
class Productos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    precio = models.FloatField()
    detalles = models.TextField(max_length=1000)
    image = models.ImageField(upload_to="productos", blank=True)
    
class Carrito(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    cantidad = models.IntegerField(default=1)
    image = models.ImageField(upload_to="carrito", blank=True)
    
    def total_precio(self):
        return self.precio * self.cantidad