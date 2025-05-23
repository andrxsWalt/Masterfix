from rest_framework import serializers
from reportes.models import Reportes, Estado_Reporte

class ReportesSerializer(serializers.ModelSerializer):
    class Meta:
        models = Reportes
        fields = ['id', 'Fecha_creacion', 'Detalle', 'Evidencia', 'Ubicacion','Tipo', 'Estado_Reporte']

class EstadoReporteSerializer(serializers.ModelSerializer):
    class Meta:
        models = Estado_Reporte
        fields = ['id', 'Nombre', 'Detalle']