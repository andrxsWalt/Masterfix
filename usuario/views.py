from django.shortcuts import render
from rest_framework import generics
from .models import Usuario, Rol, DescripcionRol
from .serializers import UsuarioSerializer, RolSerializer, DescripcionRolSerializer


class UsuarioListCreateView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
class UsuarioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer



class RolListCreateView(generics.ListCreateAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
    
class RolRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer



class DescripcionRolListCreateView(generics.ListCreateAPIView):
    queryset = DescripcionRol.objects.all()
    serializer_class = DescripcionRolSerializer
    
    
class DescripcionRolRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DescripcionRol.objects.all()
    serializer_class = DescripcionRolSerializer