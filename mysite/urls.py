"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from recetarios.views import *

urlpatterns = [
    path('', home, name='home'),
    #path('bebidas/', listar_bebidas, name='listar_bebida'),
    path('recetarios/', recetarios, name='recetarios'),
    path('recetarios/new', agregar_recetario, name='agregar_recetario'),
    path('recetarios/<int:recetario_id>/', detalle_recetario, name='detalle_recetario'),

    ### corregido
    path('bebidas/', explorar_bebidas, name='explorar_bebidas'),
    path('bebidas/<int:bebida_id>', detalle_bebida, name='detalle_bebida'),

]
