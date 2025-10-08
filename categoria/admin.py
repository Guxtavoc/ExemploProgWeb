from django.contrib import admin

from categoria.models import Categoria

class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('categoria_name',)
    }
    list_display = ('categoria_name', 'slug')

# Register your models here.
admin.site.register(Categoria,CategoriaAdmin)