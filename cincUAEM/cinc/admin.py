# -*- coding:utf8 -*-

from django.contrib import admin
from cinc.models import Investigador, Publicacion, Patente, SNI, SEI, PerfilDeseable, Tesis, Link, Aviso
from cinc.models import Estancia, Premio, ActaConsejoTecnico, Evidencia, Actividad

# Register your models here.

admin.site.register(Investigador)
admin.site.register(Publicacion)
admin.site.register(Patente)
admin.site.register(SNI)
admin.site.register(SEI)
admin.site.register(PerfilDeseable)
admin.site.register(Tesis)
admin.site.register(Estancia)
admin.site.register(Premio)
admin.site.register(ActaConsejoTecnico)
admin.site.register(Evidencia)
admin.site.register(Aviso)
admin.site.register(Actividad)
admin.site.register(Link)