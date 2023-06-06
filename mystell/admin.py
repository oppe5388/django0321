from django.contrib import admin
from .models import *

from import_export.resources import ModelResource
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats

class TaskResource(ModelResource):
    # field名とcsvの列名が異なる場合はここで指定する。

    class Meta:
        model = Task
        skip_unchanged = True
        # import_id_fields = ['day']

#インポート、エクスポート
class TaskAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'created_at', 'request_content', 'is_completed', 'response_content', 'release_date')
    resource_class = TaskResource
    list_filter = ('created_at', 'is_completed', 'release_date')
    search_fields = ('request_content', 'response_content', 'notes')

admin.site.register(Task, TaskAdmin)
    
    
