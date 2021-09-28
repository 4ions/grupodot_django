from django.db import models

# Create your models here.

class InfoUser(models.Model):
# socio, tasa, monto maximo disponible
    """ Base de datos que almacena todos los socios"""
    socio = models.CharField(max_length=60)
    tasa = models.FloatField()
    mon_max = models.IntegerField()

def __str__(self):
    return self.socio