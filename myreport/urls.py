from django.urls import path
from . import views

app_name = 'myreport'

urlpatterns = [
    # path('', views.report_list, name='report_list'),
    path('', views.report_list, name='index'),   # FBVで一覧
    path('add_fbvform', views.add_fbvform, name='add_fbvform'),   # FBVでCreate
    path('<int:pk>/', views.detail_fbvform, name='detail'),# FBVでDetail
    path('<int:pk>/update/', views.edit_fbvform, name='update'),# FBVでUpdate
    
    path('<int:pk>/add_check/', views.add_check, name='add_check'),#LDチェック関数呼び出し
]