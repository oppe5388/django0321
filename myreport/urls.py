from django.urls import path
from . import views

app_name = 'myreport'

urlpatterns = [
    path('', views.myreport, name='myreport'),
]