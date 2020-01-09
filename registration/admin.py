from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Registration

# Register your models here.
@admin.register(Registration)
class ViewAdmin(ImportExportModelAdmin):
    pass
