from django.db import models

# Create your models here.

class Consejo(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)


#Segundo crud

class Receta(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)