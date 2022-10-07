from email.policy import default
from django.db import models


class Animal(models.Model):
    referencia = models.CharField(max_length=200)
    nacimiento = models.DateTimeField('Fecha de nacimiento')
    genero = models.CharField(max_length=200)
    produccion = models.BooleanField(default=False)
    estado = models.CharField(max_length=200)
    peso = models.CharField(max_length=200)
    raza = models.CharField(max_length=200)
    obs = models.CharField(max_length=200)



class Propietario(models.Model):
    propietario = models.ForeignKey(Animal, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    CI = models.CharField(max_length=200)
    Establecimiento = models.CharField(max_length=200)
    RUC = models.CharField(max_length=200)
    departamento = models.CharField(max_length=200)
    establecimiento = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    activo = models.BooleanField(default=False)