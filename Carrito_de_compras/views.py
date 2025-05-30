from rest_framework.response import Response
from rest_framework import generics
from .models import carrito, producto
from .serializers import CarritoSerializer, ProductoSerializer

# Carrito Views
class CarritoListCreateView(generics.ListCreateAPIView):
    queryset = carrito.objects.all()
    serializer_class = CarritoSerializer

class CarritoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = carrito.objects.all()
    serializer_class = CarritoSerializer
    lookup_field = 'id'

# Producto Views
class ProductoListCreateView(generics.ListCreateAPIView):
    queryset = producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = producto.objects.all()
    serializer_class = ProductoSerializer
    lookup_field = 'id'

# Create your views here.
