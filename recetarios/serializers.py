# serializers.py
from rest_framework import serializers
from .models import Bebida, Recetario

class BebidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bebida
        fields = '__all__'


class RecetarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recetario
        fields = '__all__'

