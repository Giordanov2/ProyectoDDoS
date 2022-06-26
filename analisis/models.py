from tokenize import blank_re
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Analisis(models.Model):
    fecha = models.DateField(auto_now_add=True)
    cantidad_paquetes_analizados = models.IntegerField(null=True)
    cantidad_paquetes_normales = models.IntegerField(null=True)
    cantidad_paquetes_malignos = models.IntegerField(null=True)

    def __str__(self) :
        return self.fecha

class Paquete(models.Model):
    # analisis = id
    ip_source = models.CharField(max_length=15)
    ip_dest = models.CharField(max_length=15)
    port_source = models.IntegerField(null=True)
    port_dest = models.IntegerField(null=True)
    protocol = models.CharField(max_length=5)

class Analista(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, null=True)
    lastname = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=254, null=True)
    profile_pic = models.ImageField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self) :
        return self.name