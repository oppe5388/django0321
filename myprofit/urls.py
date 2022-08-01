from django.urls import path
from . import views

from django.views.generic import TemplateView

app_name = 'myprofit'

urlpatterns = [
    path('used02', views.used02, name='used02'),
    path('used03', views.used03, name='used03'),
    path('used04', views.used04, name='used04'),
    path('used05', views.used05, name='used05'),
    path('used05entry', views.used05entry, name='used05entry'),
    path('used06', views.used06, name='used06'),
    path('used06confirm', views.used06confirm, name='used06confirm'),
    path('used07', views.used07, name='used07'),

    path('history', views.history, name='history'),

    path('', views.profit_top, name='profit_top'),

    path('new02', views.new02, name='new02'),
    path('new03', views.new03, name='new03'),
    path('new04', views.new04, name='new04'),
    path('new05entry', views.new05entry, name='new05entry'),
    path('new05', views.new05, name='new05'),
    path('new06', views.new06, name='new06'),
    path('new06confirm', views.new06confirm, name='new06confirm'),
    path('new07', views.new07, name='new07'),

    path('service02', views.service02, name='service02'),
    path('service03', views.service03, name='service03'),
    path('service04', views.service04, name='service04'),
    path('service05entry', views.service05entry, name='service05entry'),
    path('service05', views.service05, name='service05'),
    path('service06', views.service06, name='service06'),
    path('service06confirm', views.service06confirm, name='service06confirm'),
    path('service07', views.service07, name='service07'),
    path('service01', views.service01, name='service01'),

    path('entry_example', views.entry_example, name='entry_example'),
    path('car', views.car, name='car'),

    path('search_example', views.search_example, name='search_example'),


]
