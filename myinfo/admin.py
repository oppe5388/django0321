from django.contrib import admin
from .models import *
# from django_summernote.admin import SummernoteModelAdmin

from import_export.resources import ModelResource
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats
from import_export.widgets import ForeignKeyWidget

# class InformationAdmin(SummernoteModelAdmin):
#     summernote_fields = '__all__'

class AttachmentsInline(admin.StackedInline):
    model = Attachments
    extra = 3


# class InformationAdmin(SummernoteModelAdmin, admin.ModelAdmin):
#     summernote_fields = '__all__'
#     inlines = [AttachmentsInline]


# admin.site.register(InfoCategory)


class InformationResource(ModelResource):
    class Meta:
        model = Information
        import_order = ('id', 'title')
        import_id_fields = ['id']

#お知らせインポート、エクスポート
class InformationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'created_at')  
    resource_class = InformationResource
    # formats = [base_formats.XLSX]
    search_fields = ('title', 'body')

admin.site.register(Information, InformationAdmin)


#コメント欄
class InfoCommentsAdmin(admin.ModelAdmin):
    list_display = ('comment', 'user', 'information', 'created_at')
    ordering = ('-created_at',)

admin.site.register(InfoComments, InfoCommentsAdmin)


#添付ファイル
class AttachmentsResource(ModelResource):
    class Meta:
        model = Attachments
        skip_unchanged = True
        import_id_fields = ['id']

from django.utils.safestring import mark_safe
class AttachmentsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('file_path', 'information', 'updated_at', 'thumbnail_preview')
    ordering = ('-updated_at',)

    def thumbnail_preview(self, obj):
        return mark_safe('<img src="{}" style="width:100px; height:auto;">'.format(obj.file_path.url))

    thumbnail_preview.short_description = 'プレビュー'

    #ソート
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "information":
            kwargs["queryset"] = Information.objects.all().order_by('-updated_at')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Attachments, AttachmentsAdmin)


#通知
class NotificationsAdmin(admin.ModelAdmin):
    list_display = ('user', 'information', 'created_at')
    ordering = ('-created_at',)

admin.site.register(Notifications, NotificationsAdmin)


#既読もエクスポート
class ReadStatesResource(ModelResource):
    class Meta:
        model = ReadStates
        skip_unchanged = True
        import_id_fields = ['id']

class ReadStatesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('user', 'information', 'created_at')
    ordering = ('-created_at',)

admin.site.register(ReadStates, ReadStatesAdmin)


class WorkShiftsAdmin(admin.ModelAdmin):
    list_display = ('id', 'file_path', 'created_at')
    ordering = ('-created_at',)

admin.site.register(WorkShifts, WorkShiftsAdmin)


#FAQ
class FaqsResource(ModelResource):
    class Meta:
        model = Faqs
        skip_unchanged = True
        import_id_fields = ['id']

class FaqsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'question', 'reference','created_at')  
    resource_class = FaqsResource
    filter_horizontal = ('contacts', 'attachments', 'dealers')
    search_fields = ('question', 'answer1', 'answer2')

admin.site.register(Faqs, FaqsAdmin)


class ContactsResource(ModelResource):
    # field名とcsvの列名が異なる場合はここで指定する。

    class Meta:
        model = Contacts
        skip_unchanged = True
        # import_order = ('id', 'transfer', 'deadline', 'entry', 'fix', 'setoff')
        import_id_fields = ['id']

#インポート、エクスポート
class ContactsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('incoming', 'name', 'title', 'tel', 'searchwords')
    ordering = ('id',)
    resource_class = ContactsResource
    formats = [base_formats.XLSX]
    filter_horizontal = ('attachments', 'dealers')

admin.site.register(Contacts, ContactsAdmin)


class DealersResource(ModelResource):
    class Meta:
        model = Dealers
        skip_unchanged = True
        import_id_fields = ['id']

#インポート、エクスポート
class DealersAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('code5','name')
    ordering = ('id',)
    resource_class = DealersResource
    # formats = [base_formats.XLSX]

admin.site.register(Dealers, DealersAdmin)


class ShopsResource(ModelResource):
    class Meta:
        model = Shops
        skip_unchanged = True
        import_id_fields = ['id']

#インポート、エクスポート
class ShopsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('dealer','name','shopcode', 'tel')
    ordering = ('id',)
    resource_class = ShopsResource
    # formats = [base_formats.XLSX]
    search_fields = ['name']

admin.site.register(Shops, ShopsAdmin)


#
# class ContactAttachRelResource(ModelResource):
#     class Meta:
#         model = ContactAttachRel
#         skip_unchanged = True
#         import_id_fields = ['id']

# class ContactAttachRelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#     list_display = ('contact', 'attachment')

# admin.site.register(ContactAttachRel, ContactAttachRelAdmin)