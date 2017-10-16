from django.contrib import admin
from .models import Persona

# Register your models here.

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'apellidos', 'edad', 'telefono', )