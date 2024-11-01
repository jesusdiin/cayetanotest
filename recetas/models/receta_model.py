from django.db import models

class Receta(models.Model):
    nombre = models.CharField(max_length=100)
    description = models.TextField()
    instrucciones = models.TextField()
    image = models.TextField()

    def __str__(self):
        return self.nombre