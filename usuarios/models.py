from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Genero(models.Model):
    genero = models.CharField(max_length = 30, null = False, blank = False,)
    def __str__(self):
        return self.genero
    

class Usuario(User):
    edad = models.PositiveIntegerField()
    fecha_nacimiento = models.DateTimeField()
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
