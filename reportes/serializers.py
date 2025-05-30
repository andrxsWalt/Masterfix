from rest_framework import serializers
from reportes.models import Reportes #Trae las tablas creadas en models.py

#Es un serializer por tabla


class ReportesSerializer(serializers.ModelSerializer): #El atributo es el mismo para los serializer
    class Meta:
        model = Reportes #Se especifica la tabla traída de la importación de arriba
        fields = ['id', 'Fecha_creacion', 'Detalle', 'Evidencia', 'Ubicacion','Tipo', 'Estado_Reporte'] #Se traen todos los campos más el id
