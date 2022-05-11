from django.urls import path
from . import views

from django.views.generic import TemplateView
from .views import *

app_name = 'mycontact'

urlpatterns = [
    # path('', TemplateView.as_view(template_name='mycontact/contacts_list.html'), name='contacts'),
    # path('contacts', views.ContactsJsonView.as_view(), name='ContactsJson'),
    # path('shops', TemplateView.as_view(template_name='mycontact/shops.html'), name='shops'),
    # path('shops/data', views.ShopsJsonView.as_view(), name='ShopsJson'),
]