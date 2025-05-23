from rest_framework import serializers
from reportes.models import Reportes, Estado_Reporte

class Reportesserializers(serializers.ModelSerializers):
    class Meta:
        models = Reportes
        fields = ['id', 'Fecha_creacion', 'Detalle', 'Evidencia', 'Ubicacion','Tipo', 'Estado_Reporte']

class Estado_Reporteserializers(serializers.ModelSerializers):
    class Meta:
        models = Estado_Reporte
        fields = ['id', 'Nombre', 'Detalle']