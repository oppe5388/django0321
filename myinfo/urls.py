from django.urls import path
from . import views

from django.views.generic import TemplateView
from .views import FaqsJsonView

app_name = 'myinfo'

urlpatterns = [
    path('', views.information_list, name='index'),   # FBVで一覧
    path('add_fbvform', views.add_fbvform, name='add_fbvform'),   # FBVでCreate
    path('<int:pk>/', views.detail_fbvform, name='detail'),# FBVでDetail
    path('<int:pk>/update/', views.edit_fbvform, name='update'),# FBVでUpdate
    path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),

    #通知削除関数呼び出し
    path('notifi_delete', views.notifi_delete, name='notifi_delete'),
    
    #添付ファイル削除関数呼び出し
    path('<int:pk>/attach_delete', views.attach_delete, name='attach_delete'),

    #未読削除関数呼び出し→Ajaxで未読削除
    # path('<int:pk>/read_delete', views.read_delete, name='read_delete'),
    path('<int:pk>/ajax_read_delete', views.ajax_read_delete, name="ajax_read_delete"), 

    #シフト表
    path('shift/', views.shift, name='shift'),  

    #FAQ
    path('faq/', views.faqs_list, name='faqs_list'),
    path('faq/<p>', views.faqs_tab, name='faqs_tab'),#pkみたいに渡せば共通化できるのでは？

    #FAQのDatatables未使用
    # path('faq/', TemplateView.as_view(template_name='myinfo/faqs2.html')),
    # path('faq/data', views.FaqsJsonView.as_view(), name='FaqsJson'),

    #全体検索
    path('search_result/', views.all_search, name='all_search'), 

]
