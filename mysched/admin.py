from django.contrib import admin
from .models import *

from import_export.resources import ModelResource
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats
    
class MoneyTransResource(ModelResource):
    # field名とcsvの列名が異なる場合はここで指定する。

    class Meta:
        model = MoneyTrans
        skip_unchanged = True
        # import_order = ('id', 'transfer', 'deadline', 'entry', 'fix', 'setoff')
        import_id_fields = ['transfer']

#送金スケジュールインポート、エクスポート
class MoneyTransAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'transfer', 'deadline', 'entry', 'fix', 'setoff')
    resource_class = MoneyTransResource
    formats = [base_formats.XLSX]
    list_editable = ('transfer', 'deadline', 'entry', 'fix', 'setoff')

admin.site.register(MoneyTrans, MoneyTransAdmin)