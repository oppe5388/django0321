from django import forms
from .models import *

#NFS検索の会員証番号欄
class SearchForm(forms.Form):
    keyword = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'col-6 px-0 mb-1', }))


class PostCreateForm(forms.ModelForm):
    # 親カテゴリの選択欄がないと絞り込めないので、定義する。
    parent_category = forms.ModelChoiceField(
        label='サービス商品',
        queryset=ParentCategory.objects.order_by('id'),
        empty_label='選択してください',
        required=False
    )
    
    # empty_label指定なしなら記述不要
    category = forms.ModelChoiceField(
        label='入会コース',
        queryset=Category.objects.order_by('id'),
        empty_label='選択してください',
        required=False
    )

    class Meta:
        model = Post
        fields = '__all__'

    field_order = ('title', 'parent_category', 'category')