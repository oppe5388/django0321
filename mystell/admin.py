from django.contrib import admin
from .models import *

from import_export.resources import ModelResource
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats

from django.utils.html import strip_tags

from django.utils.html import format_html
from django.utils import timezone

class TaskResource(ModelResource):
    # field名とcsvの列名が異なる場合はここで指定する。

    class Meta:
        model = Task
        skip_unchanged = True
        # import_id_fields = ['day']

#インポート、エクスポート
class TaskAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('display_image', 'get_created_at_format', 'is_completed', 'release_date', 'request_content', 'response_content', )
    # list_display = ('id', 'created_at', 'short_request_content', 'is_completed', 'short_response_content', 'release_date')
    resource_class = TaskResource
    list_filter = ('is_completed', 'release_date')
    search_fields = ('request_content', 'response_content', 'notes')
    ordering = ('id',)
    list_editable = ('request_content', 'is_completed', 'release_date', 'response_content') # 追記箇所

    # created_atフィールドのカスタム表示メソッド
    def get_created_at_format(self, obj):
        return obj.created_at.strftime('%m/%d(%a)') if obj.created_at else None
    get_created_at_format.short_description = '発生日'
    
    # 画像のプレビューを表示するカスタムメソッド
    def display_image(self, obj):
        if obj.image:
            return format_html('<a href="{}" target="_blank"><img src="{}" style="max-height:100px;max-width:60px;" /></a>', obj.image.url, obj.image.url)
        return "No Image"
    display_image.short_description = 'Image'
    
    # 未使用
    def short_request_content(self, obj):
        no_html = strip_tags(obj.request_content)
        return no_html[:50]
    short_request_content.short_description = 'Short Request Content'

    def short_response_content(self, obj):
        no_html = strip_tags(obj.response_content)
        return no_html[:50]
    short_response_content.short_description = 'Short Response Content'

admin.site.register(Task, TaskAdmin)