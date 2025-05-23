from django.shortcuts import render
from rest_framework import viewsets
from .models import Usuario, Rol, Descripción_rol
from .serializers import UsuarioSerializer, RolSerializer, DescripcionRolSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class DescripcionRolViewSet(viewsets.ModelViewSet):
    queryset = Descripción_rol.objects.all()
    serializer_class = DescripcionRolSerializer
