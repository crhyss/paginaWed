from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class inicioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['first_name','last_name','username','email','password1','password2','edad','fecha_nacimiento','genero']