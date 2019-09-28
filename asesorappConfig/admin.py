from django.contrib import admin
from asesorappConfig.models import Caso, Estudio, Notificacion, Oferta, Usuario

# Register your models here.
admin.site.register(Caso)
admin.site.register(Estudio)
admin.site.register(Notificacion)
admin.site.register(Oferta)
admin.site.register(Usuario)
