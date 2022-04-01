from django import forms
from .models import DailyReport

from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.models import User
from datetime import date, datetime

#登録（変更も同じフォームを使う）
class DailyReportForm(LoginRequiredMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['day'].initial = date.today()

        for field in self.fields.values():
            if 'class' in field.widget.attrs:
                field.widget.attrs['class'] += ' form-control mb-3'
            else:
                field.widget.attrs['class'] = 'form-control mb-3'

    class Meta:
        model = DailyReport
        fields = ['day', 'body1', 'body2', 'body3', 'body4', 'body5', 'body6', ]
        labels = {
            'day':'研修日',
            'body1':'Ⅰ.本日の研修内容',
            'body2':'Ⅱ.前回までの研修内容から、本日プラスされた知識は何ですか？',
            'body3':'Ⅲ.本日の研修内容でわかりにくかったことはありますか？',
            'body4':'Ⅳ.これまでの研修を振り返って、苦手な内容や、もう一度勉強したいこと等があれば記入してください',
            'body5':'Ⅴ.前回、(Ⅵ)で設定した目標に対して、達成できたことを記入してください（どんなに小さなことでも構いません）',
            'body6':'Ⅵ.次回の研修に臨むにあたっての目標を設定してください'
        }
        widgets = {
            'day': forms.DateInput(attrs={'type':'date'}),
        }


# #変更・更新は別→一緒なら使わない？
# class DailyReportEditForm(LoginRequiredMixin, forms.ModelForm):

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         for field in self.fields.values():
#             if 'class' in field.widget.attrs:
#                 field.widget.attrs['class'] += ' form-control'
#             else:
#                 field.widget.attrs['class'] = 'form-control'

#     class Meta:
#         model = DailyReport
#         fields = '__all__'
#         widgets = {
#             'day': forms.DateInput(attrs={'type':'date'}),
#         }

#検索
class SearchForm(forms.Form):
    keyword = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))