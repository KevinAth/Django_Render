from django.contrib import admin
from .models import Categoria,productos
# Register your models here.

admin.site.register(Categoria) ## agregamos el modelo Categoria a el panel de administracion 

# Agregamos el modelo productos al panel de administracion
@admin.register(productos)
class prodAdmin(admin.ModelAdmin):
    list_display = ("nombre","precio","categoria") # mostramos en la vista del modelo  los campos de nombre , precio y categoria.
    