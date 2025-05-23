from django.db import models
from PIL import Image #Se importa Pillow para el tipo de campo imagen


# Tabla de reportes que se registran
class Reportes(models.Model):
    Fecha_creacion = models.DateField()
    Detalle = models.CharField(max_length=100)
    Evidencia = models.ImageField(upload_to='evidencias', null=True, blank=True) #Tipo de campo imagen, que usa la librería Pillow
    Ubicacion = models.CharField(max_length=100)
    Tipo = models.CharField(max_length=100)
    Estado_Reporte = models.ForeignKey('Estado_Reporte', on_delete=models.CASCADE) #La llave foránea con la siguiente tabla
    def __str__(self):
        return self.Fecha_creacion

# Tabla del estado que pueden tener los reportes, como "Pendiente", "En Proceso" y "Solucionado"
class Estado_Reporte(models.Model):
    Nombre = models.CharField(max_length=50)
    Detalle = models.CharField(max_length=255) #Detalle de cómo va el reporte
    def __str__(self):
        return self.Nombre