from django.contrib import admin
from .models import *

from import_export.resources import ModelResource
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats

from django.utils.html import strip_tags

class TaskResource(ModelResource):
    # field名とcsvの列名が異なる場合はここで指定する。

    class Meta:
        model = Task
        skip_unchanged = True
        # import_id_fields = ['day']

#インポート、エクスポート
class TaskAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # list_display = ('id', 'created_at', 'request_content', 'is_completed', 'response_content', 'release_date')
    list_display = ('id', 'created_at', 'short_request_content', 'is_completed', 'short_response_content', 'release_date')
    resource_class = TaskResource
    list_filter = ('created_at', 'is_completed', 'release_date')
    search_fields = ('request_content', 'response_content', 'notes')
    ordering = ('id',)
    
    
    def short_request_content(self, obj):
        no_html = strip_tags(obj.request_content)
        return no_html[:30]
    short_request_content.short_description = 'Short Request Content'

    def short_response_content(self, obj):
        no_html = strip_tags(obj.response_content)
        return no_html[:30]
    short_response_content.short_description = 'Short Response Content'


admin.site.register(Task, TaskAdmin)
    
    
