from django.contrib import admin
from .models import *
# from django_summernote.admin import SummernoteModelAdmin

from import_export.resources import ModelResource
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats
from import_export.widgets import ForeignKeyWidget


def notify(modeladmin, request, queryset):
    for post in queryset:
        post.browser_push(request)


class AttachmentsInline(admin.StackedInline):
    model = Attachments
    extra = 3


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
    actions = [notify]

notify.short_description = '通知を送信する'
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
    list_filter = ['user']
    
    # informationのソート
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "information":
            kwargs["queryset"] = Information.objects.all().order_by('-id')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

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
    list_display = ('incoming', 'name', 'title', 'tel')
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
    # list_display = ('dealer','name','shopcode', 'tel')
    list_display = ('dealer','name','shopcode','tel','fax','homepage','kana')
    ordering = ('id',)
    resource_class = ShopsResource
    # formats = [base_formats.XLSX]
    search_fields = ['name']
    list_editable = ('name','shopcode','tel','fax','homepage','kana')
    list_display_links = ('dealer', )#editableでないものをリンクとして指定

admin.site.register(Shops, ShopsAdmin)


class CAsResource(ModelResource):
    class Meta:
        model = CAs
        skip_unchanged = True
        import_id_fields = ['id']

#インポート、エクスポート
class CAsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('dealer', 'shop', 'cacode', 'name')
    ordering = ('id',)
    resource_class = CAsResource
    # formats = [base_formats.XLSX]
    search_fields = ('cacode', 'name', 'kana')

admin.site.register(CAs, CAsAdmin)


#
# class ContactAttachRelResource(ModelResource):
#     class Meta:
#         model = ContactAttachRel
#         skip_unchanged = True
#         import_id_fields = ['id']

# class ContactAttachRelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#     list_display = ('contact', 'attachment')

# admin.site.register(ContactAttachRel, ContactAttachRelAdmin)


# 個人ノート
class NoteResource(ModelResource):
    class Meta:
        model = Note
        skip_unchanged = True
        import_id_fields = ['id']

#インポート、エクスポート
class NoteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('owner','title','updated_at')
    ordering = ('-updated_at',)
    resource_class = NoteResource
    search_fields = ['title','body']
    list_filter = ['owner']

admin.site.register(Note, NoteAdmin)


#ブラウザ通知
class OneSignalUserResource(ModelResource):
    class Meta:
        model = OneSignalUser
        skip_unchanged = True
        import_id_fields = ['id']

class OneSignalUserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('user', 'onesignal_user_id','created_at')
    resource_class = OneSignalUserResource

admin.site.register(OneSignalUser, OneSignalUserAdmin)


# 休業日
class HolidayResource(ModelResource):
    class Meta:
        model = Holiday
        skip_unchanged = True
        import_id_fields = ['id']

#インポート、エクスポート
class HolidayAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id','title','non_date')
    ordering = ('-non_date',)
    resource_class = HolidayResource
    list_filter = ('title','non_date')
    list_editable = ('title','non_date')

admin.site.register(Holiday, HolidayAdmin)


# FAX
class FaxResource(ModelResource):
    class Meta:
        model = Fax
        skip_unchanged = True
        import_id_fields = ['id']

#インポート、エクスポート
class FaxAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = FaxResource
    list_display = ('date','free',)
    list_editable = ('free',)

admin.site.register(Fax, FaxAdmin)


# FAX
class FaxExplainResource(ModelResource):
    class Meta:
        model = FaxExplain
        skip_unchanged = True
        import_id_fields = ['id']

#インポート、エクスポート
class FaxExplainAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('field','fax_format','id')
    resource_class = FaxExplainResource
    formats = [base_formats.XLSX]
    list_filter  = ['fax_format__name', ]
    
    # ForeignKeyをリスト出来るようにする
    def fax_format(self, obj):
        return obj.fax_format.name

admin.site.register(FaxExplain, FaxExplainAdmin)


# FAX
class FaxFormatsResource(ModelResource):
    class Meta:
        model = FaxFormats
        skip_unchanged = True
        import_id_fields = ['id']

#インポート、エクスポート
class FaxFormatsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = FaxFormatsResource

admin.site.register(FaxFormats, FaxFormatsAdmin)


# 小部屋
class RoomResource(ModelResource):
    class Meta:
        model = Room
        skip_unchanged = True
        import_id_fields = ['id']

#インポート、エクスポート
class RoomAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('date','user')
    resource_class = RoomResource

admin.site.register(Room, RoomAdmin)