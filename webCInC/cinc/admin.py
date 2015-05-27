from django.contrib import admin
from cinc.models import DatosGenerales, Publicacion, Patente, SNI, SEI, PerfilDeseable, Tesis, DireccionEstancia, Premio, ActaConsejoTecnico

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