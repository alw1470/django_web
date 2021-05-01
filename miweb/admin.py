from django.contrib import admin
from .models import Post
from .models import DatosScrapy
from import_export.admin import ImportExportModelAdmin

# admin.site.register(Post)
# admin.site.register(DatosScrapy)

@admin.register(DatosScrapy, Post)
class ViewAdmin(ImportExportModelAdmin):
    pass