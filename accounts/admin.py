from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from import_export.resources import ModelResource
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats

class UserResource(ModelResource):

    class Meta:
        model = User

class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'username', 'last_login', 'last_name', 'is_active', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    ordering = ('id', )
    resource_class = UserResource
    # formats = [base_formats.CSV]
    

admin.site.register(User, UserAdmin)


