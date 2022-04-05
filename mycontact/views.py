from django.shortcuts import render

from django.views import generic
from django_datatables_view.base_datatable_view import BaseDatatableView
from .models import Contacts


class ContactsJsonView(BaseDatatableView):
    # モデルの指定
    model = Contacts
    # 表示するフィールドの指定
    columns = ['id', 'incoming', 'name', 'tel', 'hours', 'title', 'job', 'searchwords']

    # 検索方法の指定：部分一致
    def get_filter_method(self):
        return super().FILTER_ICONTAINS