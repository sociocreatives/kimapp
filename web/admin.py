from django.contrib import admin
from .models import Legal
from .models import Faqs
from .models import ExpertTips
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(Legal, ImportExportModelAdmin)
admin.site.register(Faqs, ImportExportModelAdmin )
admin.site.register(ExpertTips, ImportExportModelAdmin)