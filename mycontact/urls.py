from django.urls import path
from . import views

from django.views.generic import TemplateView
from .views import ContactsJsonView

app_name = 'mycontact'

urlpatterns = [
    path('', TemplateView.as_view(template_name='mycontact/contacts_list.html')),
    path('contacts', views.ContactsJsonView.as_view(), name='ContactsJson'),
]