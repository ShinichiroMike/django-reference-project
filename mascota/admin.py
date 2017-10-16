from django.contrib import admin
from .models import Mascota, Vacuna
# Register your models here.

@admin.register(Mascota)
class AdminMascota(admin.ModelAdmin):
	list_display = ('id', 'nombre', 'sexo', 'edad_aproximada', 'fecha_rescate')

@admin.register(Vacuna)
class AdminVacuna(admin.ModelAdmin):
	list_display = ('nombre',)