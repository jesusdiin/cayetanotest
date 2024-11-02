from django import forms
from ..models.receta_model import Receta
from ..models.recetario_model import Recetario

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['nombre', 'instrucciones']

class RecetarioForm(forms.ModelForm):
    class Meta:
        model = Recetario
        fields = ['nombre', 'descripcion']
