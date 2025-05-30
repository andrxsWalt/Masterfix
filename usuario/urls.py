from django.urls import path
from .views import UsuarioListCreateView

urlpatterns = [
    path('usuario/', UsuarioListCreateView.as_view(), name ='UsuarioListCreate'),
]