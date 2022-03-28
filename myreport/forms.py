from django import forms
from .models import DailyReport

from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.models import User

#登録（変更も同じフォームを使う）
class DailyReportForm(LoginRequiredMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            if 'class' in field.widget.attrs:
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = DailyReport
        fields = ['day', 'body1', 'body2', 'body3', 'body4', 'body5', 'body6', ]
        widgets = {
            'day': forms.DateInput(attrs={'type':'date'}),
        }


#変更・更新は別→一緒なら使わない？
class DailyReportEditForm(LoginRequiredMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            if 'class' in field.widget.attrs:
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = DailyReport
        fields = '__all__'
        widgets = {
            'day': forms.DateInput(attrs={'type':'date'}),
        }

#検索
class SearchForm(forms.Form):
    keyword = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))


#既読チェックボックス
class CheckForm(forms.Form):
    chk1 =forms.BooleanField()
    chk2 =forms.BooleanField()
    chk3 =forms.BooleanField()
    chk4 =forms.BooleanField()