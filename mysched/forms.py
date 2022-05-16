from django import forms
from .models import MoneyTrans
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import date, datetime
# from django.contrib.admin.widgets import AdminDateWidget
# from bootstrap_datepicker_plus import DateTimePickerInput


#カレンダー選択→表示用
class MoneyForm(LoginRequiredMixin, forms.Form):
    input_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date', 'id':'input_date', 'class':'datepicker form-control form-control-user'}))
    # input_date = forms.DateField(widget=AdminDateWidget(attrs={'id':'input_date', 'class':'form-control form-control-user'}))

    # def __init__(self, *args, **kwargs):
    #         super().__init__(*args, **kwargs)

    #         self.fields['input_date'].initial = date.today()

    chotoku_date = forms.DateField(widget=forms.DateInput(attrs={'type':'month', 'id':'chotoku_date', 'class':'datepicker form-control form-control-user'}))