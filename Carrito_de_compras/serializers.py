from rest_framework import serializers
from .models import carrito, producto

class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = carrito
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = producto
        fields = '__all__'