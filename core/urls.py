
from django.urls import path
from .views import home , galeria , formulario , AgregarMascota , ListarMascota , EliminarMascota

urlpatterns = [
    path('', home, name="home"),
    path('galeria/', galeria, name="galeria"),
    path('formulario/', formulario, name="formulario"),
    path('AgregarMascota/', AgregarMascota, name="Agregar_Mascota"),
    path('ListarMascota/', ListarMascota, name="Listar_Mascota"),
    path('EliminarMascota/<id>/',EliminarMascota, name="Eliminar_Mascota"),
]