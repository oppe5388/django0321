from django.urls import path
from . import views

from django.views.generic import TemplateView

app_name = 'myprofit'

urlpatterns = [
    path('', views.profit_top, name='profit_top'),
    path('sample', views.sample, name='sample'),

]
