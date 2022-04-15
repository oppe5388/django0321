from django.urls import path
from . import views

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

    #未読削除関数呼び出し
    path('<int:pk>/read_delete', views.read_delete, name='read_delete'),

    #シフト表
    path('shift/', views.shift, name='shift'),  
]
