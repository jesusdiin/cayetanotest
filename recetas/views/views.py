import requests
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def listar_bebidas(request):
    response = requests.get("https://www.thecocktaildb.com/api/json/v1/1/filter.php?c=Cocktail")
    
    if response.status_code == 200:
        bebidas = response.json().get('drinks', [])
    else:
        bebidas = []

    return render(request, 'bebidas/bebidas_disponibles.html', {'bebidas': bebidas})
