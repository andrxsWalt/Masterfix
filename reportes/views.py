from django.shortcuts import render
from rest_framework import viewsets
from .models import Reportes, Estado_Reporte
from .serializers import ReportesSerializer, EstadoReporteSerializer

class ReportesViewSet(viewsets.ModelViewSet):
    queryset = Reportes.objects.all()
    serializer_class = ReportesSerializer

class EstadoReporteViewSet(viewsets.ModelViewSet):
    queryset = Estado_Reporte.objects.all()
    serializer_class = EstadoReporteSerializer
