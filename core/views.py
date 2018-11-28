from django.shortcuts import render, redirect

from .models import  Region, Mascota , Ciudad, Postulante, Raza, Genero , Estado, Vivienda

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def galeria(request):
    return render(request, 'core/galeria.html')

@login_required
def formulario(request):

    viviendas = Vivienda.objects.all()
    regiones = Region.objects.all()
    ciudades = Ciudad.objects.all()

    variables = {
        'viviendas':viviendas,
        'regiones': regiones,
        'ciudades': ciudades
    }

    if request.POST:
        postulante = Postulante()
        postulante.nombre = request.POST.get('txtNombre')
        postulante.run = request.POST.get('txtRun')
        postulante.fechaNacimiento = request.POST.get('txtFechaNacimiento')
        postulante.telefono = int(request.POST.get('txtTelefono'))
        postulante.correo = request.POST.get('txtCorreo')
        region = Region()
        region.id = int(request.POST.get('cboVivienda'))
        postulante.region = region
        ciudad = Ciudad()
        ciudad.id = int(request.POST.get('cboCiudad'))
        postulante.ciudad = ciudad
        vivienda = Vivienda()
        vivienda.id = int(request.POST.get('cboVivienda'))
        postulante.vivienda = vivienda

        try:
            postulante.save()
            variables['mensaje'] = 'Guardado correctamente'
        except:
            variables['mensaje'] = 'No se ha podido guardar'
    
    return render(request, 'core/formulario.html', variables)

@login_required
def AgregarMascota(request):

    raza = Raza.objects.all()
    genero = Genero.objects.all()
    estado = Estado.objects.all()

    variables = {
        'raza':raza,
        'genero': genero,
        'estado': estado
    }

    if request.POST:
        mascota = Mascota()

        mascota.nombre = request.POST.get('txtNombreMascota')

        raza = Raza()
        raza.id = request.POST.get('cboRaza')
        mascota.Raza = raza

        genero = Genero()
        genero.id = request.POST.get('cboGenero')
        mascota.Genero = genero 

        mascota.fechaIngreso = request.POST.get('txtFechaIngreso')

        mascota.fechaNacimiento = request.POST.get('txtFechaNacimiento')

        estado = Estado()
        estado.id = request.POST.get('cboEstado')
        mascota.Estado = estado

        mascota.imagen = request.FILES.get('txtimagen')

        
        try:
            mascota.save()
            variables['mensaje'] = 'Guardado correctamente'
        except:
            variables['mensaje'] = 'No se ha podido guardar'
    
    return render(request, 'core/AgregarMascota.html', variables)

def ListarMascota(request):
    #buscamos todos los automoviles
    mascota = Mascota.objects.all()

    for m in mascota:
        print(m.nombre)

    variables = {
        'mascotas':mascota  
    }

    return render(request, 'core/ListarMascota.html', variables)

def EliminarMascota(request, id):
    #primer paso encontrar el automovil
    mascota = Mascota.objects.get(id=id)

    #una vez encontrado el automovil se elimina
    try:
        mascota.delete()
        messages.success(request, 'Mascota eliminada correctamente')
    except:
        messages.error(request, 'No se ha podido eliminar')
    
    #redirigiremos al usuario de vuelta al listado
    return redirect('Listar_Mascota')

