import requests
from django.shortcuts import render, get_object_or_404, redirect


from ..models .bebida_model import Bebida
from ..models .recetario_model import Recetario

from ..forms .receta_form import RecetarioForm



def listar_bebidas(request):
    response = requests.get("https://www.thecocktaildb.com/api/json/v1/1/filter.php?c=Cocktail")
    
    if response.status_code == 200:
        bebidas = response.json().get('drinks', [])
    else:
        bebidas = []
    return render(request, 'bebidas/bebidas_disponibles.html', {'bebidas': bebidas})


def recetarios(request):
    recetarios = Recetario.objects.all()

    context = {
        'recetarios': recetarios,
        'exist_recetarios': recetarios.exists()
    }
    return render(request, 'recetarios/index.html', context)


def new_recetario(request):
    if request.method == 'POST':
        form = RecetarioForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('/recetarios/') 
    else:
        form = RecetarioForm()
    
    return render(request, 'recetarios/newrecetario.html', {'form': form})


