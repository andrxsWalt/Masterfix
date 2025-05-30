from django.db import models

class empresa (models.Model):
    nombre_empresa = models.CharField(max_length=50)
    telefono_empresa = models.IntegerField()
    email_empresa = models.EmailField(max_length=100)
    direccion_empresa = models.CharField(max_length=100)

    def _str_(self):
        return self.nombre_empresa
    
class categoria(models.Model):
    nombre_cat = models.CharField(max_length=100)
    detalles = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre_cat
    
class producto(models.Model):
    nombre_pro = models.CharField(max_length=100)
    precio = models.FloatField()
    stock = models.IntegerField()
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    fecha_ven = models.DateField()
    fecha_fab = models.DateField()

    def __str__(self):
        return self.nombre_pro

# Create your models here.
