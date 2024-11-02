from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Bebida, Recetario
from .forms import BebidaForm, RecetarioForm

import requests

def home(request):
    return render(request, 'home.html')

def explorar_bebidas(request):
    response = requests.get("https://www.thecocktaildb.com/api/json/v1/1/filter.php?c=Cocktail")
    
    if response.status_code == 200:
        bebidas = response.json().get('drinks', [])
    else:
        bebidas = []
    return render(request, 'lista_bebidas.html', {'bebidas': bebidas})

    #bebidas = Bebida.objects.all()
    #return render(request, 'lista_bebidas.html', {'bebidas': bebidas})

def agregar_bebida(request):
    if request.method == 'POST':
        form = BebidaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_bebidas')
    else:
        form = BebidaForm()
    return render(request, 'recetario/agregar_bebida.html', {'form': form})


def detalle_bebida(request, bebida_id):
    #bebida = get_object_or_404(Bebida, id=bebida_id)
    #return render(request, 'bebidas/bebida.html', {'bebida': bebida})
    url = f"https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={bebida_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data['drinks']:
            bebida_data = data['drinks'][0]
            
            nombre = bebida_data.get("strDrink")
            descripcion = bebida_data.get("strInstructions", "No hay descripción disponible.")
            imagen = bebida_data.get("strDrinkThumb")
            
            bebida_detalles = {
                "id": bebida_id,
                "nombre": nombre,
                "descripcion": descripcion,
                "imagen": imagen,
            }

            if request.method == "POST":
                Bebida.objects.create(
                    nombre=nombre,
                    descripcion=descripcion,
                    imagen=imagen,
                )
                messages.success(request, "La bebida ha sido guardada exitosamente.")
                return redirect('lista_bebidas')
            
            return render(request, 'bebidas/bebida.html', {'bebida': bebida_detalles})
        
        else:
            messages.error(request, "No se encontraron detalles para esta bebida.")
            return redirect('lista_bebidas')
    else:
        messages.error(request, "No se pudo conectar con el API .")
        return redirect('lista_bebidas')




def lista_recetarios(request):
    recetarios = Recetario.objects.all()
    return render(request, 'recetario/lista_recetarios.html', {'recetarios': recetarios})



def recetarios(request):
    recetarios = Recetario.objects.all()

    context = {
        'recetarios': recetarios,
        'exist_recetarios': recetarios.exists()
    }
    return render(request, 'recetarios.html', context)


def agregar_recetario(request):
    if request.method == 'POST':
        form = RecetarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recetarios')
    else:
        form = RecetarioForm()
    return render(request, 'new_recetario', {'form': form})
