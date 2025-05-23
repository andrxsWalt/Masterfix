from rest_framework import serializers
from usuario.models import Usuario, Rol, DescripcionRol

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        models = Usuario
        fields = ['documento', 'nombre', 'correo', 'Telefono','rol']

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        models = Rol
        fields = ['id', 'nombreRol', 'descripcionRol', 'reportes']

class DescripcionRolSerializer(serializers.ModelSerializer):
    class Meta:
        models = DescripcionRol
        fields = ['id', 'sector']