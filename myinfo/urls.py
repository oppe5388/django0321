from django.urls import path
from . import views

from django.views.generic import TemplateView
# from .views import FaqsJsonView

# from . import ajax_datatable_views

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
    # path('shift/', views.shift2, name='shift2'),  

    #FAQ
    path('faq/', views.faqs_list, name='faqs_list'),
    path('faq/<p>', views.faqs_tab, name='faqs_tab'),#pkみたいに渡せば共通化できるのでは？

    #FAQのDatatables未使用
    # path('faq/', TemplateView.as_view(template_name='myinfo/faqs2.html')),
    # path('faq/data', views.FaqsJsonView.as_view(), name='FaqsJson'),

    #全体検索
    path('search_result/', views.all_search, name='all_search'), 

    path('contacts', TemplateView.as_view(template_name='myinfo/contacts_list.html'), name='contacts'),
    path('contacts/data', views.ContactsJsonView.as_view(), name='ContactsJson'),
    # path('shops', TemplateView.as_view(template_name='myinfo/shops.html'), name='shops'),
    path('shops', views.Shops.as_view(), name='shops'),#販社一覧を渡すためにこちらに
    path('shops/data', views.ShopsJsonView.as_view(), name='ShopsJson'),
    path('shops/data2', views.ShopsJsonView2.as_view(), name='ShopsJson2'),

    #django-ajax-datatables中止
    # path('contacts', views.contacts, name="contacts"),
    # path('ajax_datatable/permissions/', ajax_datatable_views.PermissionAjaxDatatableView.as_view(),
    #      name="ajax_datatable_permissions"),

    #個人ノート
    path('note', views.note_list, name='note_list'),
    path('note_create', views.note_create, name='note_create'),
    # path('note/<int:pk>/', views.note_detail, name='note_detail'),作らない
    path('note/<int:pk>/update/', views.note_update, name='note_update'),
    path('note/<int:pk>/delete/', views.note_delete, name='note_delete'),
    path('note/<p>', views.note_tab, name='note_tab'),
    
    #個別ブラウザ通知関数
    path('onegisnal_id_create/', views.onegisnal_id_create, name="onegisnal_id_create"), 

    #FAX当番
    # path('fax/', views.fax, name='fax'),
    # path('fax/<p>/', views.fax, name='fax'),
    path('fax/<str:p>/', views.fax, name='fax'),
    path('fax/<p>/delete/', views.fax_delete, name='fax_delete'),
    path('fax/<p>/update/', views.fax_del_create, name='fax_del_create'),
    path('fax/<p>/ajax_room_add', views.ajax_room_add, name="ajax_room_add"), #小部屋希望追加
    path('fax/<p>/ajax_room_delete', views.ajax_room_delete, name="ajax_room_delete"), #小部屋希望削除
    path('fax/<p>/ajax_day_move/', views.ajax_day_move, name="ajax_day_move"), #ajax前後日付移動
    path('fax/<p>/edit/', views.fax_edit, name="fax_edit"), #sortable不可のためedit画面を別に用意
    
    #FAXルール
    # path('faxrule/<p>/', views.fax_rule, name='fax_rule'),
    path('faxrule/', views.fax_rule, name='fax_rule'),

]
