from django import forms
from .models import Contacts
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import date, datetime


#
class ContactsForm(LoginRequiredMixin, forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ('incoming', 'name', 'title', 'job', 'tel', 'hours', 'searchwords')