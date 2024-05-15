from django.contrib import admin
from .models import Legal
from .models import Faqs
from .models import ExpertTips
from .models import Category
from .models import Tvets
from .models import Profile
from .models import SubCategory
from .models import WhyChoose
from import_export.admin import ImportExportModelAdmin


# Register your models here.
admin.site.register(Legal, ImportExportModelAdmin)
admin.site.register(Faqs, ImportExportModelAdmin )
admin.site.register(ExpertTips, ImportExportModelAdmin)
admin.site.register(Category, ImportExportModelAdmin)
admin.site.register(Tvets, ImportExportModelAdmin)
admin.site.register(Profile, ImportExportModelAdmin)
admin.site.register(SubCategory, ImportExportModelAdmin)
admin.site.register(WhyChoose, ImportExportModelAdmin)

