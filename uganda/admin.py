from django.contrib import admin
from .models import CategoryUganda
from .models import SubCategoryUganda, Colleges
from import_export.admin import ImportExportModelAdmin


# Register your models here.
admin.site.register(CategoryUganda, ImportExportModelAdmin)
admin.site.register(Colleges, ImportExportModelAdmin)
admin.site.register(SubCategoryUganda, ImportExportModelAdmin)

