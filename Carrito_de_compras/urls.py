from django.urls import path
from .views import (
    CarritoListCreateView, CarritoRetrieveUpdateDestroyView,
    ProductoListCreateView, ProductoRetrieveUpdateDestroyView,
)

urlpatterns = [
    # Carrito endpoints
    path('carritos/', CarritoListCreateView.as_view(), name='carrito-list-create'),
    path('carritos/<int:id>/', CarritoRetrieveUpdateDestroyView.as_view(), name='carrito-detail'),

    # Producto endpoints
    path('productos/', ProductoListCreateView.as_view(), name='producto-list-create'),
    path('productos/<int:id>/', ProductoRetrieveUpdateDestroyView.as_view(), name='producto-detail'),
]
