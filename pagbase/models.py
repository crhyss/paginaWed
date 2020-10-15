from django.db import models

# Create your models here.
class Producto(models.Model):
    link = models.URLField()
    nombre = models.CharField(max_length=50,null=False,blank=False)
    marca = models.CharField(max_length=50,null=False,blank=False)
    modelo = models.CharField(max_length=50,null=False,blank=False)
    precio = models.PositiveIntegerField()
    peso = models.PositiveIntegerField()
    dimension = models.PositiveIntegerField()
    detalle = models.TextField(max_length=300)

# class Categoria(models.Model):
#     tecnologia =  