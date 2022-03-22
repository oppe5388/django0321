from django.urls import path
from . import views

app_name = 'myinfo'

urlpatterns = [
    # path('', views.index, name='index'),
    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('create/', views.CreateView.as_view(), name='create'),
    # path('<int:pk>/update/', views.UpdateView.as_view(), name='update'),
    
    path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),
    path('add_post', views.add_post, name='add_post'),   # インラインフォームセット
    # path('<int:pk>/update/', views.update_post, name='update_post'),

    path("formview_test", views.aaa.as_view(), name="formview_test"),

    path('export/', views.post_export, name='export'),

    # path('create_comment', views.create_comment, name='create_comment'),   # コメントポスト

    path('fileuptest', views.upload_file, name='fileuptest'),#`ファイルUPテスト用`

    path('', views.information_list, name='index'),   # FBVで一覧
    path('add_fbvform', views.add_fbvform, name='add_fbvform'),   # FBVでCreate
    path('<int:pk>/', views.detail_fbvform, name='detail'),# FBVでDetail
    path('<int:pk>/update/', views.edit_fbvform, name='update'),# FBVでUpdate

    #通知削除関数呼び出し
    path('notifi_delete', views.notifi_delete, name='notifi_delete'),
    
    #添付ファイル削除関数呼び出し
    path('<int:pk>/attach_delete', views.attach_delete, name='attach_delete'),

    # #コメント投稿
    # path('<int:pk>/comment_post', views.comment_post, name='comment_post'),

]
