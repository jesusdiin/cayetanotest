from django.db import models

class Recetario(models.Model):
    nombre = models.CharField(max_length=255)
    def __str__(self):
        return self.nombre

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Dimension(models.Model):
    tipo = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.tipo

class Bebida(models.Model):
    nombre = models.CharField(max_length=100)
    instrucciones = models.TextField()
    ingredientes = models.ManyToManyField(Ingrediente, related_name='bebidas')
    categorias = models.ManyToManyField(Categoria, related_name='bebidas')
    recetarios = models.ManyToManyField(Recetario, through='RecetarioBebida')
    dimension = models.ForeignKey(Dimension, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre

class RecetarioBebida(models.Model):
    recetario = models.ForeignKey(Recetario, on_delete=models.CASCADE)
    bebida = models.ForeignKey(Bebida, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('recetario', 'bebida')
