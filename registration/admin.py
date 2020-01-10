from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Registration, Contact

# Register your models here.
@admin.register(Registration, Contact)
class ViewAdmin(ImportExportModelAdmin):
    pass
