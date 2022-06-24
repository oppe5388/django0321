from django.urls import path
from . import views

from django.views.generic import TemplateView

app_name = 'myprofit'

urlpatterns = [
    path('', views.profit_top, name='profit_top'),
    path('new01', views.new01, name='new01'),
    path('new02', views.new02, name='new02'),
    path('new03', views.new03, name='new03'),
    path('new04', views.new04, name='new04'),

]
