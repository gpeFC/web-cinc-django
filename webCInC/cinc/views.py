from django.shortcuts import render, render_to_response
from django.template.loader import get_template
from django.template import Context, Template, RequestContext
from django.http import HttpResponse
from cinc.models import Tesis, ActaConsejoTecnico

# Create your views here.

def bdcinc(request):
	plantilla = get_template('bdcinc.html')
	html = plantilla.render(Context({'argumento':'Django'}))
	return HttpResponse(html)

def inicio2(request):
	tesis = Tesis.objects.all()
	return render_to_response('inicio.html', {'tesis':tesis}, context_instance=RequestContext(request))

def inicio(request):
	plantilla = get_template('inicio.html')
	html = plantilla.render(Context())
	return HttpResponse(html)

def cinc(request):
	plantilla = get_template('cinc.html')
	html = plantilla.render(Context())
	return HttpResponse(html)

def investigacion(request):
	plantilla = get_template('investigacion.html')
	html = plantilla.render(Context())
	return HttpResponse(html)

def investigadores(request):
	plantilla = get_template('investigadores.html')
	html = plantilla.render(Context())
	return HttpResponse(html)

def lineas_investigacion(request):
	plantilla = get_template('lineasinvestigacion.html')
	html = plantilla.render(Context())
	return HttpResponse(html)

def publicaciones(request):
	plantilla = get_template('publicaciones.html')
	html = plantilla.render(Context())
	return HttpResponse(html)

def administracion(request):
	plantilla = get_template('administracion.html')
	html = plantilla.render(Context())
	return HttpResponse(html)

def actas(request):
	actas = ActaConsejoTecnico.objects.all()
	return render_to_response('actas.html', {'actas':actas}, context_instance=RequestContext(request))

def oferta_educativa(request):
	plantilla = get_template('ofertaeducativa.html')
	html = plantilla.render(Context())
	return HttpResponse(html)

def acerca_de(request):
	plantilla = get_template('acercade.html')
	html = plantilla.render(Context())
	return HttpResponse(html)

def oferta_educativa(request):
	plantilla = get_template('ofertaeducativa.html')
	html = plantilla.render(Context())
	return HttpResponse(html)

def departamentos(request):
	plantilla = get_template('departamentos.html')
	html = plantilla.render(Context())
	return HttpResponse(html)