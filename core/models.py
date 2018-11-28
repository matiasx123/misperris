from django.db import models

class Vivienda(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion

class Region(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Region"
        verbose_name_plural= "Regiones"

class Ciudad(models.Model):
    nombre = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural= "Ciudades"

class Postulante(models.Model):
    nombre = models.CharField(max_length=300)
    run = models.CharField(max_length=12, unique=True)
    fechaNacimiento = models.DateField(verbose_name='Fecha de Nacimiento')
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    vivienda = models.ForeignKey(Vivienda, on_delete=models.CASCADE)
    telefono = models.IntegerField()
    correo = models.EmailField()

    def __str__(self):
        return self.run

class Raza(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Genero(models.Model):
    descripcion = models.CharField(max_length = 50)
    def __str__(self):
        return self.descripcion

class Estado(models.Model):
    descripcion = models.CharField(max_length = 50)
    def __str__(self):
        return self.descripcion

class Mascota(models.Model):
    nombre = models.CharField(max_length = 100)
    raza =  models.ForeignKey(Raza, on_delete=models.CASCADE)
    #genero = models.ForeignKey(Genero, on_delete = models.CASCADE)
    fechaIngreso = models.DateField()
    fechaNacimiento = models.DateField()
    estado = models.ForeignKey(Estado, on_delete = models.CASCADE)
    imagen = models.ImageField(upload_to="MascotaIMG",null =True)
    
    def __str__(self):
        return self.nombre
   
