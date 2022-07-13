from django.urls import path
from . import views

from django.views.generic import TemplateView

app_name = 'myprofit'

urlpatterns = [
    path('used02', views.used02, name='used02'),
    path('used03', views.used03, name='used03'),
    path('used04', views.used04, name='used04'),
    path('used05', views.used05, name='used05'),
    path('used06', views.used06, name='used06'),
    path('used07', views.used07, name='used07'),

    path('history', views.history, name='history'),


    path('', views.profit_top, name='profit_top'),
    path('new01', views.new01, name='new01'),
    path('new02', views.new02, name='new02'),
    path('new03', views.new03, name='new03'),
    path('new04', views.new04, name='new04'),
    path('new05', views.new05, name='new05'),
    path('new06', views.new06, name='new06'),
    path('new07', views.new07, name='new07'),
    path('new08', views.new08, name='new08'),
    path('new01_02', views.new01_02, name='new01_02'),
    path('new02_02', views.new02_02, name='new02_02'),
    path('new03_02', views.new03_02, name='new03_02'),
    path('new04_02', views.new04_02, name='new04_02'),
    path('new07_02', views.new07_02, name='new07_02'),
    path('new01_03', views.new01_03, name='new01_03'),
    path('new02_03', views.new02_03, name='new02_03'),
    path('new04_03', views.new04_03, name='new04_03'),
    path('new05_03', views.new05_03, name='new05_03'),
    path('new06_03', views.new06_03, name='new06_03'),
    path('new07_03', views.new07_03, name='new07_03'),

    path('service01_01', views.service01_01, name='service01_01'),
    path('service02_01', views.service02_01, name='service02_01'),
    path('service03_01', views.service03_01, name='service03_01'),
    path('service03_02', views.service03_02, name='service03_02'),
    path('service04_01', views.service04_01, name='service04_01'),
    path('service04_03', views.service04_03, name='service04_03'),
    path('service07_01', views.service07_01, name='service07_01'),
    
]
