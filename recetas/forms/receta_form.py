from django import forms
from ..models.receta_model import Receta

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['nombre', 'instrucciones']
