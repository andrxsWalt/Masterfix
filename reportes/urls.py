from django.urls import path, include # Importa la función path para definir rutas y include para incluir otras URLs
from rest_framework.routers import DefaultRouter #Router de Django
from .views import ReportesListCreateView, EstadoReporteListCreateView #Importa las vistas de las tablas

router = DefaultRouter()
router.register(r'reportes', ReportesListCreateView) #Registra un endpoint llamado "reportes" en el cual se usa la vista de Reportes
router.register(r'estados', EstadoReporteListCreateView) #Lo mismo, llamado "estados" y manejado por EstadoReportes

urlpatterns = [ #Define las urls en este módulo
    path('', include(router.urls)), #Agrega las URLS automáticas del router
]