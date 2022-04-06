from django.shortcuts import render

from django.views import generic
from django_datatables_view.base_datatable_view import BaseDatatableView
from .models import Contacts
from django.db.models import Q


class ContactsJsonView(BaseDatatableView):
    # モデルの指定
    model = Contacts
    # 表示するフィールドの指定
    columns = ['id', 'incoming', 'name', 'tel', 'hours', 'title', 'job', 'searchwords']

    # # 検索方法の指定：部分一致
    # def get_filter_method(self):
    #     return super().FILTER_ICONTAINS


    def filter_queryset(self, qs):
        # # use parameters passed in GET request to filter queryset

        # # simple example:
        # search = self.request.GET.get('search[value]', None)
        # if search:
        #     qs = qs.filter(name__istartswith=search)

        # # more advanced example using extra parameters
        # filter_customer = self.request.GET.get('customer', None)

        # if filter_customer:
        #     customer_parts = filter_customer.split(' ')
        #     qs_params = None
        #     for part in customer_parts:
        #         q = Q(customer_firstname__istartswith=part) | Q(customer_lastname__istartswith=part)
        #         qs_params = qs_params | q if qs_params else q
        #     qs = qs.filter(qs_params)
        # return qs


        search = self.request.GET.get('search[value]', None)
        if search:
            search_parts = search.split()
            for part in search_parts:
                qs = qs.filter(
                        Q(incoming__icontains=part) | 
                        Q(name__icontains=part) | 
                        Q(title__icontains=part) | 
                        Q(job__icontains=part) | 
                        Q(tel__icontains=part) | 
                        Q(hours__icontains=part) | 
                        Q(searchwords__icontains=part)
                    )
        return qs