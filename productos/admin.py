from django.contrib import admin
from .models import *

class ComercialAdmin(admin.ModelAdmin):
    fields = ('comercial_name',)

class TitleAdmin(admin.ModelAdmin):
    fields = ('title_name',)

class UsuarioAdmin(admin.ModelAdmin):
    fields = ('usuario_name', 'password',)

class ProductosAdmin(admin.ModelAdmin):
    fields = ('productos_name','productos_comercial','productos_title',)

admin.site.register(Comercial, ComercialAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Productos, ProductosAdmin)
admin.site.register(Usuario, UsuarioAdmin)