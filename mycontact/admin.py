from django.contrib import admin
from .models import *

from import_export.resources import ModelResource
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats
    
class ContactsResource(ModelResource):
    # field名とcsvの列名が異なる場合はここで指定する。

    class Meta:
        model = Contacts
        skip_unchanged = True
        # import_order = ('id', 'transfer', 'deadline', 'entry', 'fix', 'setoff')
        import_id_fields = ['id']

#インポート、エクスポート
class ContactsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('incoming', 'name', 'title', 'job', 'tel', 'hours', 'searchwords')
    resource_class = ContactsResource

admin.site.register(Contacts, ContactsAdmin)