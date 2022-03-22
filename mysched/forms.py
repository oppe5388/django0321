from django import forms
from .models import MoneyTrans
from django.contrib.auth.mixins import LoginRequiredMixin


#カレンダー選択→表示用
class MoneyForm(LoginRequiredMixin, forms.Form):
    input_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))