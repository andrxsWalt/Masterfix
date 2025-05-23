from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Reportes, Estado_Reporte

admin.site.register(Reportes)
admin.site.register(Estado_Reporte)
