from django import forms
from .models import Producto
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['foto','nombre','marca','modelo','precio','peso','dimension','detalle','categoria']