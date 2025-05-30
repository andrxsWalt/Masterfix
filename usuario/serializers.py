from rest_framework import serializers
from usuario.models import Usuario, Rol, persona

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['documento', 'nombre', 'correo', 'telefono','rol']
        
class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['nombre', 'descepcion']


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = persona
        fields = ['nombre', 'correo', 'contraseña', 'rol']