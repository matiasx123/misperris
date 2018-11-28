from django.contrib import admin
from .models import Vivienda,Region,Ciudad,Postulante,Raza,Genero,Estado,Mascota
# Register your models here.

class PostulanteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'run', 'fechaNacimiento', 'region', 'ciudad', 'vivienda', 'telefono', 'correo')
    search_fields =['run']
admin.site.register(Vivienda)
admin.site.register(Region)
admin.site.register(Ciudad)
admin.site.register(Postulante, PostulanteAdmin)


class AgregarMascota(admin.ModelAdmin):
    list_display=('nombre','raza','genero','fechaIngreso','fechaNacimiento','estado')
    search_fields =['nombre']
admin.site.register(Raza)
admin.site.register(Genero)
admin.site.register(Estado)
admin.site.register(Mascota,AgregarMascota)



