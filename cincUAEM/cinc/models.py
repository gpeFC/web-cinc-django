from django.db import models

# Create your models here.

class Aviso(models.Model):
	titulo = models.CharField(max_length=50)
	fecha = models.DateField()
	descripcion = models.CharField(max_length=500)
	link = models.CharField(null=True, max_length=500)

	def __unicode__(self):
		return self.titulo

class Actividad(models.Model):
	titulo = models.CharField(max_length=50)
	fecha = models.DateField()
	descripcion = models.CharField(max_length=500)
	imagen = models.ImageField(null=True, upload_to="imagenesActividades")
	link = models.CharField(null=True, max_length=500)
	archivo_pdf = models.FileField(null=True, upload_to="archivosActividades")

	def __unicode__(self):
		return self.titulo

class Link(models.Model):
	titulo = models.CharField(max_length=50)
	fecha = models.DateField()
	link = models.CharField(null=True, max_length=500)

	def __unicode__(self):
		return self.titulo

class Miscelaneo(models.Model):
	titulo = models.CharField(max_length=50)
	fecha = models.DateField()
	descripcion = models.CharField(max_length=500)
	imagen = models.ImageField(null=True, upload_to="imagenesMiscelaneos")
	link = models.CharField(null=True, max_length=500)
	archivo_pdf = models.FileField(null=True, upload_to="archivosMiscelaneos")

	def __unicode__(self):
		return self.titulo

class Evidencia(models.Model):
	titulo = models.CharField(max_length=50)
	fecha = models.DateField()
	descripcion = models.CharField(max_length=500)
	imagen = models.ImageField(upload_to="imagenesEvidencias")
	link_video = models.CharField(null=True, max_length=500)
	archivo_pdf = models.FileField(null=True, upload_to="archivosEvidencias")

	def __unicode__(self):
		return self.titulo

class ActaConsejoTecnico(models.Model):
	fecha = models.CharField(max_length=10,default="DD/MM/AAAA")
	numero = models.IntegerField(null=True)
	archivo_pdf = models.FileField(null=True, upload_to="actasConsejoTecnico")

	def __unicode__(self):
		return "Acta %s - %s" % (self.numero, self.fecha)

class DatosGenerales(models.Model):
	nombre = models.CharField(max_length=75)
	nivel = models.CharField(max_length=10)
	definitivo = models.CharField(max_length=2)
	fecha_ingreso_uaem = models.CharField(max_length=4)
	departamento = models.CharField(max_length=11)
	email = models.EmailField(null=True)
	foto = models.ImageField(null=True, upload_to="fotosInvestigadores")

	def __unicode__(self):
		return self.nombre

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

	def __unicode__(self):
		return "%s - %s" % (self.titulo, self.anio)

class Patente(models.Model):
	titulo = models.CharField(null=True, max_length=150)
	anio = models.CharField(max_length=4)
	referencia = models.TextField()
	pitc_s = models.TextField()
	estatus = models.CharField(max_length=10)
	archivo_pdf = models.FileField(null=True, upload_to="patentes")

	def __unicode__(self):
		return "%s - %s" % (self.titulo, self.anio)


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