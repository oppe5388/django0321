from django.urls import path
from . import views
from .views import ContactsList, ContactsListJson

app_name = 'mycontact'

urlpatterns = [
    # path('', views.ContactsJsonView.as_view(), name='ContactsJson'),
    # url(r'^testmodel$', TestModelList.as_view(), name="testmodel"),
    path('', ContactsList.as_view(), name="contacts"),
]