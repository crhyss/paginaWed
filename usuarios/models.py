from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Usuario(User):
    edad = models.PositiveIntegerField()
    fecha_nacimiento = models.DateTimeField()
    genero = models.CharField(max_length = 30, null = False, blank = False)