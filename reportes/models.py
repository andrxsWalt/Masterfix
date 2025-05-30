from django.db import models
from PIL import Image #Se importa Pillow para el tipo de campo imagen


# Tabla de reportes que se registran
class Reportes(models.Model):
    Fecha_creacion = models.DateField()
    Detalle = models.CharField(max_length=100)
    Evidencia = models.ImageField(upload_to='evidencias', null=True, blank=True) #Tipo de campo imagen, que usa la librería Pillow
    Ubicacion = models.CharField(max_length=100)
    Tipo = models.CharField(max_length=100)
    #Permite controlar el estado de los reportes
    ESTADO_PENDIENTE= "Pendiente"
    ESTADO_EnProceso= "En proceso"
    ESTADO_Solucionado= "Solucionado" #Nuevo estado agregado para mayor granularidad

    ESTADO_CHOICES=[
        (ESTADO_PENDIENTE, "Pendiente"),
        (ESTADO_EnProceso, "En proceso"),
        (ESTADO_Solucionado, "Solucionado"), #Puede ver usuarios, pero no modificarlos
    ]
    Estado_Reporte = models.CharField(
        max_length=15,
        choices=ESTADO_CHOICES,
        default=ESTADO_PENDIENTE, #Por defecto, los nuevos reportes serán estado pendiente
        help_text="Define en que estado se encuentra el reporte"
    )
    def __str__(self):
        return self.Fecha_creacion
