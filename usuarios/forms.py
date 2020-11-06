from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.models import User

def agregarClaseFormControl(elementos):
    for campo in elementos:
        campo.field.widget.attrs['class'] = 'form-control'

class inicioForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm,self).__init__(*args, **kwargs)
        agregarClaseFormControl(self.visible_fields())
    class Meta:
        model = Usuario
        fields = ('first_name','last_name','username','password1','password2','email','edad','fecha_nacimiento','genero')
        widgets = {
            "fecha_nacimiento":forms.TextInput(
                attrs={
                    "type":"date"
                }
            )
        }

class restablecerContraseniaForm(PasswordResetForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'ingrese su nombre de usuario',
        'class':'form-control',
    }))
    