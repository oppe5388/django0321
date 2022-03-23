from django import forms
from .models import MoneyTrans
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import date, datetime


#カレンダー選択→表示用
class MoneyForm(LoginRequiredMixin, forms.Form):
    input_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))

    # def __init__(self, *args, **kwargs):
    #         super().__init__(*args, **kwargs)

    #         self.fields['input_date'].initial = date.today()