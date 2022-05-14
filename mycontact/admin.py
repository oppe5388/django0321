from django.contrib import admin
from .models import *

# from import_export.resources import ModelResource
# from import_export.admin import ImportExportModelAdmin
# from import_export.formats import base_formats
# from import_export.widgets import ForeignKeyWidget
    
# class ContactsResource(ModelResource):
#     # field名とcsvの列名が異なる場合はここで指定する。

#     class Meta:
#         model = Contacts
#         skip_unchanged = True
#         # import_order = ('id', 'transfer', 'deadline', 'entry', 'fix', 'setoff')
#         import_id_fields = ['id']

# #インポート、エクスポート
# class ContactsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#     list_display = ('incoming', 'name', 'title', 'job', 'tel', 'hours', 'searchwords')
#     resource_class = ContactsResource
#     formats = [base_formats.XLSX]

# admin.site.register(Contacts, ContactsAdmin)


# class DealersResource(ModelResource):
#     class Meta:
#         model = Dealers
#         skip_unchanged = True
#         import_id_fields = ['id']

# #インポート、エクスポート
# class DealersAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#     list_display = ('code5','name')
#     ordering = ('id',)
#     resource_class = DealersResource
#     # formats = [base_formats.XLSX]

# admin.site.register(Dealers, DealersAdmin)


# class ShopsResource(ModelResource):
#     class Meta:
#         model = Shops
#         skip_unchanged = True
#         import_id_fields = ['id']

# #インポート、エクスポート
# class ShopsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#     list_display = ('dealer','name','shopcode', 'tel')
#     ordering = ('id',)
#     resource_class = ShopsResource
#     # formats = [base_formats.XLSX]
#     search_fields = ['name']

# admin.site.register(Shops, ShopsAdmin)