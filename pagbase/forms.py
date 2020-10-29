from django import forms
from .models import Producto,Categoria

def agregarClaseFormControl(elementos):
    for campo in elementos:
        campo.field.widget.attrs['class'] = 'form-control'

class ProductoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductoForm,self).__init__(*args, **kwargs)
        agregarClaseFormControl(self.visible_fields())
        
    class Meta:
        model = Producto
        fields = ['foto','nombre','marca','modelo','precio','peso','dimension','detalle','categoria']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['Nombre']