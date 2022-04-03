from django.urls import path
from . import views

app_name = 'mysched'

urlpatterns = [
    path('', views.mysched, name='mysched'),
    path('fixdisp', views.mysched_fixdisp, name='fixdisp'),
    # path('', views.information_list, name='index'),
]