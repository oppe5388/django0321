from django.contrib import admin
from .models import *

from import_export.resources import ModelResource
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats
    
class DailyReportResource(ModelResource):
    # field名とcsvの列名が異なる場合はここで指定する。

    class Meta:
        model = DailyReport
        skip_unchanged = True
        import_id_fields = ['day']

#お知らせインポート、エクスポート
class DailyReportAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('day', 'user')
    resource_class = DailyReportResource

admin.site.register(DailyReport, DailyReportAdmin)

#LDチェック
class CheckStatesAdmin(admin.ModelAdmin):
    list_display = ('user', 'report')

admin.site.register(CheckStates, CheckStatesAdmin)

#既読
class ReportReadAdmin(admin.ModelAdmin):
    list_display = ('user', 'report')

admin.site.register(ReportRead, ReportReadAdmin)