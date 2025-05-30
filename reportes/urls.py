from django.urls import path
from .views import ReportesListCreateView
 # Importa la función path para definir rutas y include para incluir otras URLs
from rest_framework.routers import DefaultRouter #Router de Django
from .views import ReportesListCreateView #Importa las vistas de las tablas


urlpatterns = [ #Define las urls en este módulo
    path('reporte/', ReportesListCreateView.as_view(), name= 'ReportesListCreateView'), 
    #Agrega las URLS automáticas del router
]