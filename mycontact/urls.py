from django.urls import path
from . import views
# from .views import ContactsList, ContactsListJson

from django.views.generic import TemplateView
from .views import ContactsListJson

app_name = 'mycontact'

urlpatterns = [
    # path('', views.ContactsJsonView.as_view(), name='ContactsJson'),
    # url(r'^testmodel$', TestModelList.as_view(), name="testmodel"),
    # path('', ContactsList.as_view(), name="contacts"),
    path('', TemplateView.as_view(template_name='mycontact/contacts_list.html')),
    path('data/', ContactsListJson.as_view()),
]