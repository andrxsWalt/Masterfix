from django.shortcuts import render
from rest_framework import viewsets
from .models import Usuario, Rol, DescripciónRol
from .serializers import UsuarioSerializer, RolSerializer, DescripciónRolSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class DescripcionRolViewSet(viewsets.ModelViewSet):
    queryset = DescripciónRol.objects.all()
    serializer_class = DescripciónRolSerializer
