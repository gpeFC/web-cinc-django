from django.db import models

# Create your models here.

class ActaConsejoTecnico(models.Model):
	fecha = models.CharField(max_length=9)
	descripcion = models.CharField(null=True, max_length=150)
	archivo_pdf = models.FileField(null=True, upload_to="actasConsejoTecnico")

class DatosGenerales(models.Model):
	nombre = models.CharField(max_length=75)
	nivel = models.CharField(max_length=10)
	definitivo = models.CharField(max_length=2)
	fecha_ingreso_uaem = models.CharField(max_length=4)
	departamento = models.CharField(max_length=11)
	email = models.EmailField(null=True)
	foto = models.ImageField(null=True, upload_to="fotosInvestigadores")

class Publicacion(models.Model):
	anio = models.CharField(max_length=4)
	tipo = models.CharField(max_length=30)
	indizada_jcr = models.CharField(max_length=2)
	con_alumnos = models.CharField(max_length=2)
	titulo = models.CharField(max_length=150)
	autores = models.TextField()
	publicacion = models.CharField(max_length=8)
	volumen = models.IntegerField()
	numero = models.IntegerField()
	paginas = models.CharField(max_length=9)
	issn_isbn = models.CharField(max_length=30)
	doi = models.CharField(max_length=50)
	archivo_pdf = models.FileField(null=True, upload_to="publicaciones")

class Patente(models.Model):
	anio = models.CharField(max_length=4)
	referencia = models.TextField()
	pitc_s = models.TextField()
	estatus = models.CharField(max_length=10)
	archivo_pdf = models.FileField(null=True, upload_to="patentes")


class SNI(models.Model):
	nivel = models.CharField(max_length=3)
	vigencia = models.CharField(max_length=9)
	nombramiento_pdf = models.FileField(null=True, upload_to="sni")

class SEI(models.Model):
	tiene = models.CharField(max_length=2)
	archivo_pdf = models.FileField(null=True, upload_to="sei")

class PerfilDeseable(models.Model):
	vigencia = models.CharField(max_length=9)
	nombramiento_pdf = models.FileField(null=True, upload_to="perfilDeseable")

class Tesis(models.Model):
	anio = models.CharField(max_length=4)
	nivel = models.CharField(max_length=12)
	archivo_pdf = models.FileField(null=True, upload_to="tesis")

class DireccionEstancia(models.Model):
	tipo = models.CharField(max_length=12)
	visitante = models.CharField(max_length=2)
	duracion = models.CharField(max_length=9)
	archivo_pdf = models.FileField(null=True, upload_to="direccionEstancia")

class Premio(models.Model):
	anio = models.CharField(max_length=4)
	descripcion = models.TextField()
	comprobante_pdf = models.FileField(null=True, upload_to="premios")