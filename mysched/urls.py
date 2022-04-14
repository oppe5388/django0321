from django.urls import path
from . import views

app_name = 'mysched'

urlpatterns = [
    path('', views.mysched, name='mysched'),
    # path('', views.information_list, name='index'),
]