# -*- coding:utf8 -*-

from django.db import models

# Create your models here.

class Investigador(models.Model):
	nombre = models.CharField(max_length=75, verbose_name="Nombre")
	nivel = models.CharField(max_length=12, verbose_name="Nivel")
	definitivo = models.CharField(max_length=2, verbose_name="¿Definitivo?")
	anio_ingreso_uaem = models.CharField(max_length=4, blank=True, verbose_name="Año de ingreso(UAEM)?")
	departamento = models.CharField(max_length=11, verbose_name="Departamento")
	email = models.EmailField(blank=True, verbose_name="Correo eletrónico")
	foto = models.ImageField(blank=True, upload_to="fotosInvestigadores", verbose_name="Fotografía")

	class Meta:
		ordering = ["nombre"]
		verbose_name_plural = "Investigadores"

	def __unicode__(self):
		return self.nombre

class Publicacion(models.Model):
	anio = models.CharField(max_length=4, verbose_name="Año")
	tipo = models.CharField(max_length=30, verbose_name="Tipo")
	indizada_jcr = models.CharField(max_length=2, blank=True, verbose_name="¿Indizada en el JCR?")
	incluye_alumnos = models.CharField(max_length=2, blank=True, verbose_name="¿Incluye alumnos?")
	titulo = models.CharField(max_length=150, verbose_name="Titulo")
	autores = models.ManyToManyField(Investigador, verbose_name="Autores")
	volumen = models.IntegerField(blank=True, verbose_name="Volumen")
	numero = models.IntegerField(blank=True, verbose_name="Número")
	paginas = models.CharField(max_length=9, verbose_name="Páginas")
	issn_isbn = models.CharField(max_length=10, verbose_name="ISSN/ISBN")
	doi = models.CharField(max_length=15, verbose_name="DOI")
	pdf = models.FileField(upload_to="publicaciones", verbose_name="Archivo PDF")

	class Meta:
		ordering = ["anio"]
		verbose_name_plural = "Publicaciones"

	def __unicode__(self):
		return "%s - %s" % (self.titulo, self.anio)

class Patente(models.Model):
	titulo = models.CharField(max_length=150, blank=True, verbose_name="Titulo")
	anio = models.CharField(max_length=4, verbose_name="Año")
	referencia = models.TextField(verbose_name="Referencia")
	pitcs = models.ManyToManyField(Investigador, verbose_name="PITCs")
	estatus = models.CharField(max_length=10, verbose_name="Estatus")
	pdf = models.FileField(upload_to="patentes", verbose_name="Archivo PDF")

	class Meta:
		ordering = ["anio"]
		verbose_name_plural = "Patentes"

	def __unicode__(self):
		return "%s - %s" % (self.titulo, self.anio)

class SNI(models.Model):
	investigador = models.OneToOneField(Investigador, verbose_name="Investigador")
	nivel = models.CharField(max_length=3, verbose_name="Nivel")
	vigencia = models.CharField(max_length=10, verbose_name="Vigencia")
	pdf = models.FileField(upload_to="sni", verbose_name="Nombramiento(PDF)")

	class Meta:
		ordering = ["investigador"]
		verbose_name_plural = "SNIs"

	def __unicode__(self):
		return self.investigador

class SEI(models.Model):
	investigador = models.OneToOneField(Investigador, verbose_name="Investigador")
	vigencia = models.CharField(max_length=10, verbose_name="Vigencia")
	pdf = models.FileField(upload_to="sei", verbose_name="Archivo PDF")

	class Meta:
		ordering = ["investigador"]
		verbose_name_plural = "SEIs"

	def __unicode__(self):
		return self.investigador

class PerfilDeseable(models.Model):
	investigador = models.ForeignKey(Investigador, verbose_name="Investigador")
	vigencia = models.CharField(max_length=10, verbose_name="Vigencia")
	pdf = models.FileField(upload_to="perfilDeseable", verbose_name="Nombramiento(PDF)")

	class Meta:
		ordering = ["investigador"]
		verbose_name_plural = "Perfil Deseable"

	def __unicode__(self):
		return self.investigador

class Tesis(models.Model):
	investigadores = models.ManyToManyField(Investigador, verbose_name="Investigadores")
	titulo = models.CharField(max_length=150, blank=True, verbose_name="Titulo")
	anio = models.CharField(max_length=4, verbose_name="Año")
	nivel = models.CharField(max_length=12, verbose_name="Nivel")
	pdf = models.FileField(upload_to="tesis", verbose_name="Archivo de tesis(PDF)")

	class Meta:
		ordering = ["titulo"]
		verbose_name_plural = "Tesis"

	def __unicode__(self):
		return "%s - %s" % (self.titulo, self.anio)

class Estancia(models.Model):
	investigador = models.OneToOneField(Investigador, verbose_name="Investigador")
	tipo = models.CharField(max_length=12, verbose_name="Tipo de estancia")
	duracion = models.CharField(max_length=21, verbose_name="Duración")
	pdf = models.FileField(upload_to="estancia", verbose_name="Archivo PDF")

	class Meta:
		ordering = ["investigador"]
		verbose_name_plural = "Estancias"

	def __unicode__(self):
		return self.investigador

class Premio(models.Model):
	investigadores = models.ManyToManyField(Investigador, verbose_name="Investigadores")
	titulo = models.CharField(max_length=150, blank=True, verbose_name="Titulo el premio")
	anio = models.CharField(max_length=4, verbose_name="Año")
	descripcion = models.TextField(blank=True, verbose_name="Descripción")
	pdf = models.FileField(upload_to="premios", verbose_name="Comprobante(PDF)")

	class Meta:
		ordering = ["anio"]
		verbose_name_plural = "Premios"

	def __unicode__(self):
		return "%s - %s" % (self.titulo, self.anio)

class ActaConsejoTecnico(models.Model):
	fecha = models.CharField(max_length=10, verbose_name="Fecha")
	numero = models.IntegerField(verbose_name="N°")
	pdf = models.FileField(upload_to="actasConsejoTecnico", verbose_name="Archivo de acta(PDF)")

	class Meta:
		ordering = ["numero"]
		verbose_name_plural = "Actas de Consejo Técnico"

	def __unicode__(self):
		return "Acta N°: %d" % (self.numero)

class Evidencia(models.Model):
	titulo = models.CharField(max_length=150, verbose_name="Titulo")
	fecha = models.DateField(verbose_name="Fecha")
	descripcion = models.CharField(max_length=500, blank=True, verbose_name="Descripción")
	imagen = models.ImageField(upload_to="imagenesEvidencias", blank=True, verbose_name="Imagen/Fotografía")
	video = models.URLField(blank=True, verbose_name="Link a video")
	pdf = models.FileField(upload_to="archivosEvidencias", blank=True, verbose_name="Archivo PDF")

	class Meta:
		ordering = ["fecha"]
		verbose_name_plural = "Evidencias"

	def __unicode__(self):
		return self.titulo

class Aviso(models.Model):
	titulo = models.CharField(max_length=75, verbose_name="Titulo")
	fecha = models.DateField(verbose_name="Fecha")
	descripcion = models.CharField(max_length=150, verbose_name="Descripción")
	link = models.URLField(blank=True, verbose_name="Link a aviso")
	pdf = models.FileField(upload_to="archivosAvisos", blank=True, verbose_name="Archivo PDF")

	class Meta:
		ordering = ["fecha"]
		verbose_name_plural = "Avisos"

	def __unicode__(self):
		self.titulo

class Actividad(models.Model):
	titulo = models.CharField(max_length=75, verbose_name="Titulo")
	fecha = models.DateField(verbose_name="Fecha")
	descripcion = models.CharField(max_length=150, verbose_name="Descripción")
	imagen = models.ImageField(upload_to="imagenesActividades", blank=True, verbose_name="Imagen/Fotografía")
	link = models.URLField(blank=True, verbose_name="Link a actividad")
	pdf = models.FileField(upload_to="archivosActividades", blank=True, verbose_name="Archivo PDF")

	class Meta:
		ordering = ["fecha"]
		verbose_name_plural = "Actividades"

	def __unicode__(self):
		return self.titulo

class Link(models.Model):
	titulo = models.CharField(max_length=75, verbose_name="Titulo")
	fecha = models.DateField(verbose_name="Fecha")
	link = models.URLField(blank=True, verbose_name="Link")

	class Meta:
		ordering = ["fecha"]
		verbose_name_plural = "Links"

	def __unicode__(self):
		self.titulo