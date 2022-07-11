from django import forms

#NFS検索の会員証番号欄
class SearchForm(forms.Form):
    keyword = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'col-6 px-0 mb-1', }))