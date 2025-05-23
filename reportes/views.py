from django.shortcuts import render
from rest_framework import generics
from .models import Reportes, Estado_Reporte
from .serializers import ReportesSerializer, EstadoReporteSerializer

class ReportesListCreateView(generics.ListCreateAPIView):
    queryset = Reportes.objects.all() #Los QuerySet son objetos que guardan los datos de lo que se le especefica. En este caso, trae todo de la tabla reportes.
    serializer_class = ReportesSerializer #Define el serializer de la tabla creado en el archivo de serializers

    
class ReportesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reportes.objects.all() #Los QuerySet son objetos que guardan los datos de lo que se le especefica. En este caso, trae todo de la tabla reportes.
    serializer_class = ReportesSerializer #Define el serializer de la tabla creado en el archivo de serializers


class EstadoReporteListCreateView(generics.ListCreateAPIView):
    queryset = Estado_Reporte.objects.all()
    serializer_class = EstadoReporteSerializer


class EstadoReporteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estado_Reporte.objects.all()
    serializer_class = EstadoReporteSerializer