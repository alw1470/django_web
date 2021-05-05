from django.contrib import admin
from .models import Post
from .models import Categorias
from .models import DatosScrapy
from import_export.admin import ImportExportModelAdmin

admin.site.register(Categorias)

@admin.register(DatosScrapy, Post)
class ViewAdmin(ImportExportModelAdmin):
    pass