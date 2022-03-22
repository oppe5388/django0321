from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin

# class InformationAdmin(SummernoteModelAdmin):
#     summernote_fields = '__all__'

class AttachmentsInline(admin.StackedInline):
    model = Attachments
    extra = 3


class InformationAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    summernote_fields = '__all__'
    inlines = [AttachmentsInline]


admin.site.register(InfoCategory)
# admin.site.register(ReadStates)
# admin.site.register(Notifications)
# admin.site.register(InfoComments)
# admin.site.register(Attachments)

from import_export.resources import ModelResource
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats

class InformationResource(ModelResource):
    class Meta:
        model = Information
        import_order = ('id', 'title')
        import_id_fields = ['id']

#お知らせインポート、エクスポート
class InformationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'body', 'created_at')  
    resource_class = InformationResource
    # formats = [base_formats.CSV]

admin.site.register(Information, InformationAdmin)


#コメント欄
class InfoCommentsAdmin(admin.ModelAdmin):
    list_display = ('comment', 'user', 'information', 'created_at')
    ordering = ('-created_at',)

admin.site.register(InfoComments, InfoCommentsAdmin)


#添付ファイル
from django.utils.safestring import mark_safe
class AttachmentsAdmin(admin.ModelAdmin):
    list_display = ('file_path', 'information', 'created_at', 'thumbnail_preview')
    ordering = ('-created_at',)

    def thumbnail_preview(self, obj):
        return mark_safe('<img src="{}" style="width:100px; height:auto;">'.format(obj.file_path.url))

    thumbnail_preview.short_description = 'プレビュー'

admin.site.register(Attachments, AttachmentsAdmin)


#通知
class NotificationsAdmin(admin.ModelAdmin):
    list_display = ('user', 'information', 'created_at')
    ordering = ('-created_at',)

admin.site.register(Notifications, NotificationsAdmin)


#既読
class ReadStatesAdmin(admin.ModelAdmin):
    list_display = ('user', 'information', 'created_at')
    ordering = ('-created_at',)

admin.site.register(ReadStates, ReadStatesAdmin)
