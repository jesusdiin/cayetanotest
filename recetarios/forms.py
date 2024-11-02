from django import forms
from .models import Bebida, Recetario

class BebidaForm(forms.ModelForm):
    class Meta:
        model = Bebida
        fields = ['nombre', 'instrucciones', 'ingredientes', 'categorias', 'dimension']

class RecetarioForm(forms.ModelForm):
    class Meta:
        model = Recetario
        fields = ['nombre']
