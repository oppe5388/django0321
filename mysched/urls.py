from django.urls import path
from . import views

app_name = 'mysched'

urlpatterns = [
    path('', views.mysched, name='mysched'),
    # path('', views.information_list, name='index'),
    path('ajax_sched/', views.ajax_sched, name="ajax_sched"), 
    path('chotoku_calc/', views.chotoku_calc, name="chotoku_calc"), 
]