from django.views import generic
from django_datatables_view.base_datatable_view import BaseDatatableView

from .models import Item


# DataTablesにデータを提供するWebAPI
# django-datatables-view
# https://pypi.org/project/django-datatables-view/
class ItemsJsonView(BaseDatatableView):
    # モデルの指定
    model = Item
    # フィールドの指定
    columns = ['id', 'pref_name', 'name', 'furigana', 'zipcode', 'address', 'tel', 'code']

    # 検索方法の指定：部分一致
    def get_filter_method(self):
        return super().FILTER_ICONTAINS