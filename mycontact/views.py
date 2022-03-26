from django.shortcuts import render

# Create your views here.

from django.views import generic
from django.views.generic import TemplateView
from django_datatables_view.base_datatable_view import BaseDatatableView
from .models import Contacts
from .forms import ContactsForm


# class ContactsList(TemplateView):
#     # template_name = 'mycontact/contacts_list.html'
#     template_name = 'mycontact/tables.html'


class ContactsListJson(BaseDatatableView):
    model = Contacts
    
    # 検索方法の指定：部分一致
    def get_filter_method(self):
        return super().FILTER_ICONTAINS

# class ContactsJsonView(BaseDatatableView):
#     # モデルの指定
#     model = Contacts
#     # 表示するフィールドの指定
#     columns = ['incoming', 'name', 'title', 'job', 'tel', 'hours', 'searchwords']


#     # 検索方法の指定：部分一致
#     def get_filter_method(self):
#         return super().FILTER_ICONTAINS