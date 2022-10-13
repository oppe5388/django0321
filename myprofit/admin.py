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
    list_display = ('id', 'name')
    ordering = ('id',)
    resource_class = ParentCategoryResource

admin.site.register(ParentCategory, ParentCategoryAdmin)

# 入会コース
class CategoryResource(ModelResource):
    class Meta:
        model = Category
        skip_unchanged = True
        import_id_fields = ['id']

class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'name', 'parent')
    ordering = ('id',) 
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


# プルダウン用車種クラス
class ClassDropResource(ModelResource):
    class Meta:
        model = ClassDrop
        skip_unchanged = True
        import_id_fields = ['id']

class ClassDropAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('id',)
    resource_class = ClassDropResource

admin.site.register(ClassDrop, ClassDropAdmin)

# プルダウンに紐付いた車名
class CarDropResource(ModelResource):
    class Meta:
        model = CarDrop
        skip_unchanged = True
        import_id_fields = ['id']

class CarDropAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'name', 'base_digit', 'parent')
    resource_class = CarDropResource

admin.site.register(CarDrop, CarDropAdmin)


# メーカー
class MakerResource(ModelResource):
    class Meta:
        model = Maker
        skip_unchanged = True

class MakerAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = MakerResource

admin.site.register(Maker, MakerAdmin)


# 乗用ボディタイプ
class PassengerTypeResource(ModelResource):
    class Meta:
        model = PassengerType
        skip_unchanged = True

class PassengerTypeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = PassengerTypeResource

admin.site.register(PassengerType, PassengerTypeAdmin)


# 乗用サイズ
class PassengerSizeResource(ModelResource):
    class Meta:
        model = PassengerSize
        skip_unchanged = True

class PassengerSizeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = PassengerSizeResource

admin.site.register(PassengerSize, PassengerSizeAdmin)


# 商用ボディタイプ
class CargoTypeResource(ModelResource):
    class Meta:
        model = CargoType
        skip_unchanged = True

class CargoTypeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CargoTypeResource

admin.site.register(CargoType, CargoTypeAdmin)


# 商用サイズ
class CargoSizeResource(ModelResource):
    class Meta:
        model = CargoSize
        skip_unchanged = True

class CargoSizeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CargoSizeResource

admin.site.register(CargoSize, CargoSizeAdmin)

# 車名（価格用）
class CarForPriceResource(ModelResource):
    class Meta:
        model = CarForPrice
        skip_unchanged = True

class CarForPriceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'maker', 'remarks', 'base_digit', 'code',  'passenger_type', 'passenger_size', 'cargo_type', 'cargo_size')
    ordering = ('id',)
    resource_class = CarForPriceResource
    search_fields = ('name', 'base_digit',)

admin.site.register(CarForPrice, CarForPriceAdmin)