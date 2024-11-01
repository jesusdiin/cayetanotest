from django.shortcuts import render, get_object_or_404

from ..models.receta_model import Receta
from ..forms.receta_form import RecetaForm

def listar_recetas(request):
    recetas = Receta.objects.all()
    return render(request, 'recetas/lista_recetas.html', {'recetas': recetas})
