from django.urls import path
from . import views

app_name = 'mycontact'

urlpatterns = [
    path('', views.ContactsJsonView.as_view(), name='ContactsJson'),
]