from django.db import models
from PIL import Image

#Comentario prueba

# Create your models here.
class Reportes(models.Model):
    Fecha_creacion = models.DateField()
    Detalle = models.CharField(max_length=100)
    Evidencia = models.ImageField(upload_to='evidencias', null=True, blank=True)
    Ubicacion = models.CharField(max_length=100)
    Tipo = models.CharField(max_length=100)
    Estado_Reporte = models.ForeignKey('Estado_Reporte', on_delete=models.CASCADE)
    def __str__(self):
        return self.Fecha_creacion

class Estado_Reporte(models.Model):
    Nombre = models.CharField(max_length=50)
    Detalle = models.CharField(max_length=255)
    def __str__(self):
        return self.Nombre
    
# Comentario de prueba