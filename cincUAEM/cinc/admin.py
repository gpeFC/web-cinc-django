from django.contrib import admin
from cinc.models import DatosGenerales, Publicacion, Patente, SNI, SEI, PerfilDeseable, Tesis, Link, Aviso
from cinc.models import DireccionEstancia, Premio, ActaConsejoTecnico, Evidencia, Actividad

# Register your models here.

admin.site.register(DatosGenerales)
admin.site.register(Publicacion)
admin.site.register(Patente)
admin.site.register(SNI)
admin.site.register(SEI)
admin.site.register(PerfilDeseable)
admin.site.register(Tesis)
admin.site.register(DireccionEstancia)
admin.site.register(Premio)
admin.site.register(ActaConsejoTecnico)
admin.site.register(Evidencia)
admin.site.register(Aviso)
admin.site.register(Actividad)
admin.site.register(Link)