#visatas basadas en clases

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Bebida, Recetario, RecetarioBebida
from .forms import BebidaForm, RecetarioForm

import requests


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Bebida
from .serializers import BebidaSerializer

class BebidaList(APIView):
    def get(self, request):
        response = requests.get("https://www.thecocktaildb.com/api/json/v1/1/filter.php?c=Cocktail")
        if response.status_code == 200:
            bebidas = response.json().get('drinks', [])
            # Procesar las bebidas para el formato deseado
            bebidas_procesadas = [
                {
                    "nombre": bebida.get("strDrink"),
                    "imagen": bebida.get("strDrinkThumb"),
                    "id": bebida.get("idDrink"),
                }
                for bebida in bebidas
            ]
            return Response(bebidas_procesadas, status=status.HTTP_200_OK)

        return Response({"error": "No se pudieron obtener las bebidas"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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

            recetarios = Recetario.objects.all()

            if request.method == "POST":
                recetario_id = request.POST.get('recetario_id')
                recetario = get_object_or_404(Recetario, id=recetario_id)

                bebida, created = Bebida.objects.get_or_create(
                    nombre=nombre,
                    defaults={'descripcion': descripcion, 'imagen': imagen}
                )

                print(f"Bebida creada: {created}")

                association, assoc_created = RecetarioBebida.objects.get_or_create(bebida=bebida, recetario=recetario)

                print(f"RecetarioBebida creada: {assoc_created}")

                if assoc_created:
                    messages.success(request, f"La bebida '{nombre}' ha sido guardada en el recetario '{recetario.nombre}' exitosamente.")
                else:
                    messages.info(request, f"La bebida '{nombre}' ya estaba en el recetario '{recetario.nombre}'.")

                return redirect('detalle_bebida', bebida_id=bebida_id)

            return render(request, 'detalle_bebida.html', {'bebida': bebida_detalles, 'recetarios': recetarios})
        
        else:
            messages.error(request, "No se encontró la bebida seleccionada en la API.")
            return redirect('lista_bebidas')
    else:
        messages.error(request, "No se pudo conectar con el API.")
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
    return render(request, 'new_recetario.html', {'form': form})


def detalle_recetario(request, recetario_id):
    recetario = get_object_or_404(Recetario, id=recetario_id)
    
    bebidas = RecetarioBebida.objects.filter(recetario=recetario).select_related('bebida')

    context = {
        'recetario': recetario,
        'bebidas': bebidas,
    }
    return render(request, 'detalle_recetario.html', context)


def guardar_bebida_en_recetario(request, bebida_id):
    if request.method == "POST":
            recetario_id = request.POST.get("recetario_id")
            recetario = get_object_or_404(Recetario, id=recetario_id)

            try:
                bebida = Bebida.objects.get(id=bebida_id)
                recetario.bebidas.add(bebida)
                messages.success(request, f"La bebida '{bebida.nombre}' ha sido añadida a '{recetario.nombre}'.")
            except Bebida.DoesNotExist:
                messages.error(request, "No se encontró la bebida seleccionada.")

    return redirect('detalle_bebida', bebida_id=bebida_id)
