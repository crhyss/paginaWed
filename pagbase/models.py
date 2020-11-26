from django.db import models

# Create your models here.
class Categoria(models.Model):
    Nombre = models.CharField(max_length = 30, null = False, blank = False,)
    def __str__(self):
        return self.Nombre
class Producto(models.Model):
    foto = models.FileField(upload_to='fotos')
    nombre = models.CharField(max_length=50,null=False,blank=False)
    marca = models.CharField(max_length=50,null=False,blank=False)
    modelo = models.CharField(max_length=50,null=False,blank=False)
    precio = models.PositiveIntegerField()
    peso = models.PositiveIntegerField()
    dimension = models.PositiveIntegerField()
    detalle = models.TextField(max_length=300)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

