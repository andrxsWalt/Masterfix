from django.shortcuts import render
from rest_framework import viewsets
from .models import Reportes, Estado_Reporte
from .serializers import ReportesSerializer, EstadoReporteSerializer

class ReportesViewSet(viewsets.ModelViewSet):
    queryset = Reportes.objects.all() #Los QuerySet son objetos que guardan los datos de lo que se le especefica. En este caso, trae todo de la tabla reportes.
    serializer_class = ReportesSerializer #Define el serializer de la tabla creado en el archivo de serializers

class EstadoReporteViewSet(viewsets.ModelViewSet):
    queryset = Estado_Reporte.objects.all()
    serializer_class = EstadoReporteSerializer
