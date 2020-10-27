from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class inicioForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm,self).__init__(*args, **kwargs)
        for campo in self.visible_fields():
            campo.field.widget.attrs['class'] = 'form_control'
    class Meta:
        model = Usuario
        fields = ('first_name','last_name','username','password1','password2','email','edad','fecha_nacimiento','genero')
