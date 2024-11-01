from django.db import models

class Recetario(models.Model):
    nombre = models.CharField(max_length=100)
    description = models.TextField()
    image = models.TextField()
    recetas = models.TextField()

    def __str__(self):
        return self.nombre