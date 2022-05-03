from django.shortcuts import render

from django.views import generic
from django_datatables_view.base_datatable_view import BaseDatatableView
from .models import *
from django.db.models import Q
import operator
from django.utils.html import escape


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


class DealersJsonView(BaseDatatableView):
    # モデルの指定
    model = Dealers
    # 表示するフィールドの指定
    columns = ['id', 'code5', 'code4', 'name', 'full_name', 'domain', 'customer_desk',	'emergency', 'bc', 'nfs', 'in_house', 'base', 'base_tel']

    def filter_queryset(self, qs):

        search = self.request.GET.get('search[value]', None)
        if search:
            search_parts = search.split()
            for part in search_parts:
                qs = qs.filter(
                        Q(code5__icontains=part) | 
                        Q(code4__icontains=part) | 
                        Q(name__icontains=part) | 
                        Q(full_name__icontains=part) | 
                        Q(domain__icontains=part) | 
                        Q(customer_desk__icontains=part) | 
                        Q(emergency__icontains=part) | 
                        Q(bc__icontains=part) | 
                        Q(nfs__icontains=part) | 
                        Q(in_house__icontains=part) | 
                        Q(base__icontains=part) | 
                        Q(base_tel__icontains=part)
                    )
        return qs

class ShopsJsonView(BaseDatatableView):
    model = Shops
    # columns = ['id', 'dealer', 'name', 'shopcode', 'tel', 'fax', 'homepage', 'memo', 'kana']
    # ↓でソートはOKでも、検索でエラー
    columns = ['id', 'dealer__name', 'name', 'shopcode', 'tel', 'fax', 'homepage', 'memo', 'kana']
    def render_column(self, row, column):
        if column == 'dealer__name':
            return row.dealer.name
        else:
            return super(ShopsJsonView, self).render_column(row, column)

    # https://pypi.org/project/django-datatables-view/1.20.0/
    # 動作OK
    # def render_column(self, row, column):
    #     if column == 'custom':
    #         return f'{row.dealer}'
    #     else:
    #         return super(ShopsJsonView, self).render_column(row, column)

    # ↓外部キー検索できない、窓口一覧と同じもの
    def filter_queryset(self, qs):

        search = self.request.GET.get('search[value]', None)
        if search:
            search_parts = search.split()
            for part in search_parts:
                #外部キー検索できる？
                # query = reduce(operator.and_, [ Q(dealer__name__icontains=part) for part in qs ] )
                # qs = qs.filter( query )

                qs = qs.filter(
                        # Q(dealer__icontains=part) | #これがあるとエラーになる
                        Q(dealer__name__icontains=part) | #これがあるとエラーになる
                        Q(name__icontains=part) | 
                        Q(shopcode__icontains=part) | 
                        Q(tel__icontains=part) | 
                        Q(fax__icontains=part) | 
                        Q(homepage__icontains=part) | 
                        Q(memo__icontains=part) | 
                        Q(kana__icontains=part)
                    )
        return qs


#↓テストでソートできた
# class ShopsJsonView(BaseDatatableView):
#     model = Shops
#     columns = [
#         'id',
#         'dealer__name',
#         'name',
#     ]

#     def render_column(self, row, col):
#         if col == 'dealer__name':
#             return row.dealer.name
#         return super().render_column(row, col)