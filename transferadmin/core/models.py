from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre= models.CharField(max_length=30, verbose_name='Nombre')
    rut= models.CharField(primary_key=True, max_length=15, verbose_name='Rut')
    ciudad= models.CharField(max_length=15, verbose_name='Ciudad')
    comuna= models.CharField(max_length=15, verbose_name='Comuna')
    direccion= models.CharField(max_length=40, verbose_name='Direccion')

    def __str__(self):
        return self.rut

class Transfer(models.Model):
    numero= models.IntegerField(verbose_name='Numero de transfer')
    asiento= models.IntegerField(verbose_name='Asientos disponibles')
    hora= models.CharField(max_length=5, verbose_name='Hora salida')
    patente= models.CharField(primary_key=True, max_length= 6, verbose_name='Patente')
    nombreChofer= models.CharField(max_length=30, verbose_name='Nombre Chofer')

    def __str__(self):
        return self.patente