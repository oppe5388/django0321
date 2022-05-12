# from django.shortcuts import render

# from django.views import generic
# from django_datatables_view.base_datatable_view import BaseDatatableView
# from .models import *
# from django.db.models import Q
# import operator
# from django.utils.html import escape


# class ContactsJsonView(BaseDatatableView):
#     # モデルの指定
#     model = Contacts
#     # 表示するフィールドの指定
#     columns = ['id', 'incoming', 'name', 'tel', 'hours', 'title', 'job', 'searchwords']

#     # # 検索方法の指定：部分一致
#     # def get_filter_method(self):
#     #     return super().FILTER_ICONTAINS


#     def filter_queryset(self, qs):
#         # # use parameters passed in GET request to filter queryset

#         # # simple example:
#         # search = self.request.GET.get('search[value]', None)
#         # if search:
#         #     qs = qs.filter(name__istartswith=search)

#         # # more advanced example using extra parameters
#         # filter_customer = self.request.GET.get('customer', None)

#         # if filter_customer:
#         #     customer_parts = filter_customer.split(' ')
#         #     qs_params = None
#         #     for part in customer_parts:
#         #         q = Q(customer_firstname__istartswith=part) | Q(customer_lastname__istartswith=part)
#         #         qs_params = qs_params | q if qs_params else q
#         #     qs = qs.filter(qs_params)
#         # return qs


#         search = self.request.GET.get('search[value]', None)
#         if search:
#             search_parts = search.split()
#             for part in search_parts:
#                 qs = qs.filter(
#                         Q(incoming__icontains=part) | 
#                         Q(name__icontains=part) | 
#                         Q(title__icontains=part) | 
#                         Q(job__icontains=part) | 
#                         Q(tel__icontains=part) | 
#                         Q(hours__icontains=part) | 
#                         Q(searchwords__icontains=part)
#                     )
#         return qs


# class DealersJsonView(BaseDatatableView):
#     # モデルの指定
#     model = Dealers
#     # 表示するフィールドの指定
#     columns = ['id', 'code5', 'code4', 'name', 'full_name', 'domain', 'customer_desk',	'emergency', 'bc', 'nfs', 'in_house', 'base', 'base_tel']

#     # 検索方法の指定：ワード1つならこれだけでOK
#     def get_filter_method(self):
#         return super().FILTER_ICONTAINS


# class ShopsJsonView(BaseDatatableView):
#     model = Shops
#     # columns = ['id', 'dealer', 'name', 'shopcode', 'tel', 'fax', 'homepage', 'memo', 'kana']
#     # ↓でソートはOKでも、検索でエラー
#     columns = [
#         'id',
#         'dealer__name',
#         'name',
#         'shopcode',
#         'tel',
#         'fax',
#         'homepage',
#         'memo',
#         'kana',
#         'dealer__pk',
#         'dealer__code5',
#         'dealer__code4',
#         'dealer__full_name',
#         'dealer__domain',
#         'dealer__customer_desk',
#         'dealer__emergency',
#         'dealer__bc',
#         'dealer__nfs',
#         'dealer__in_house',
#         'dealer__base',
#         'dealer__base_tel',
#         ]
#     def render_column(self, row, column):
#         if column == 'dealer__name':
#             return row.dealer.name
#             # return row.dealer.pk #pkも返せる
#         elif column == 'dealer__pk':
#             return row.dealer.pk
#         elif column == 'dealer__code5':
#             return row.dealer.code5
#         elif column == 'dealer__code4':
#             return row.dealer.code4
#         elif column == 'dealer__full_name':
#             return row.dealer.full_name
#         elif column == 'dealer__domain':
#             return row.dealer.domain
#         elif column == 'dealer__customer_desk':
#             return row.dealer.customer_desk
#         elif column == 'dealer__emergency':
#             return row.dealer.emergency
#         elif column == 'dealer__bc':
#             return row.dealer.bc
#         elif column == 'dealer__nfs':
#             return row.dealer.nfs
#         elif column == 'dealer__in_house':
#             return row.dealer.in_house
#         elif column == 'dealer__base':
#             return row.dealer.base
#         elif column == 'dealer__base_tel':
#             return row.dealer.base_tel
#         else:
#             return super(ShopsJsonView, self).render_column(row, column)

#     # https://pypi.org/project/django-datatables-view/1.20.0/
#     # 動作OK
#     # def render_column(self, row, column):
#     #     if column == 'custom':
#     #         return f'{row.dealer}'
#     #     else:
#     #         return super(ShopsJsonView, self).render_column(row, column)

#     # 複数ワード
#     def filter_queryset(self, qs):

#         search = self.request.GET.get('search[value]', None)
#         if search:
#             search_parts = search.split()
#             for part in search_parts:
#                 #外部キー検索できる？
#                 # query = reduce(operator.and_, [ Q(dealer__name__icontains=part) for part in qs ] )
#                 # qs = qs.filter( query )

#                 qs = qs.filter(
#                         # Q(dealer__icontains=part) | #これがあるとエラーになる
#                         Q(dealer__name__icontains=part) | #これでOK
#                         Q(name__icontains=part) | 
#                         Q(shopcode__icontains=part) | 
#                         Q(tel__icontains=part) | 
#                         Q(fax__icontains=part) | 
#                         Q(homepage__icontains=part) | 
#                         Q(memo__icontains=part) | 
#                         Q(kana__icontains=part)
#                     )
#         return qs


# #↓テストでソートできた
# # class ShopsJsonView(BaseDatatableView):
# #     model = Shops
# #     columns = [
# #         'id',
# #         'dealer__name',
# #         'name',
# #     ]

# #     def render_column(self, row, col):
# #         if col == 'dealer__name':
# #             return row.dealer.name
# #         return super().render_column(row, col)