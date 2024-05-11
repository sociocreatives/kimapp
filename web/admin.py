from django.contrib import admin
from .models import Legal
from .models import Faqs
from .models import ExpertTips
from .models import Category
from .models import MajorCategory
from .models import Tvets
from .models import Profile
from import_export.admin import ImportExportModelAdmin


# Register your models here.
admin.site.register(Legal, ImportExportModelAdmin)
admin.site.register(Faqs, ImportExportModelAdmin )
admin.site.register(ExpertTips, ImportExportModelAdmin)
admin.site.register(Category, ImportExportModelAdmin)
admin.site.register(MajorCategory, ImportExportModelAdmin)
admin.site.register(Tvets, ImportExportModelAdmin)
admin.site.register(Profile, ImportExportModelAdmin)