from django.contrib import admin
from .models import *

from import_export.resources import ModelResource
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats
from import_export.widgets import ForeignKeyWidget

# サービス商品
class ParentCategoryResource(ModelResource):
    class Meta:
        model = ParentCategory
        skip_unchanged = True
        import_id_fields = ['id']

class ParentCategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ParentCategoryResource

admin.site.register(ParentCategory, ParentCategoryAdmin)

# 入会コース
class CategoryResource(ModelResource):
    class Meta:
        model = Category
        skip_unchanged = True
        import_id_fields = ['id']

class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CategoryResource

admin.site.register(Category, CategoryAdmin)


# 投稿
class PostResource(ModelResource):
    class Meta:
        model = Post
        skip_unchanged = True
        import_id_fields = ['id']

class PostAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = PostResource

admin.site.register(Post, PostAdmin)