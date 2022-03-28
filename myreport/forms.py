from django import forms
from .models import DailyReport

from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.models import User

#登録（変更も同じフォームを使う）
class DailyReport(LoginRequiredMixin, forms.ModelForm):

    class Meta:
        model = Information
        fields = '__all__'


#検索
class SearchForm(forms.Form):
    keyword = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))


#既読チェックボックス
class ReadForm(forms.Form):
    chk1 =forms.BooleanField()
    chk2 =forms.BooleanField()
    chk3 =forms.BooleanField()
    chk4 =forms.BooleanField()
        

#変更・更新は別→使わない？
class DailyReportEditForm(LoginRequiredMixin, forms.ModelForm):

    class Meta:
        model = Information
        fields = '__all__'