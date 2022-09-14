from django import forms
from .models import *

# from django_summernote.widgets import SummernoteWidget
from django.contrib.auth.mixins import LoginRequiredMixin

# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
from accounts.models import User


from .widgets import CustomCheckboxSelectMultiple
from .widgets import AccordionCheckbox

from tinymce.widgets import TinyMCE  #追加
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

#登録
class InformationForm(LoginRequiredMixin, forms.ModelForm):

    ## クラス変数として宣言だけしておく。
    # tags = None
    tags = forms.ModelMultipleChoiceField(
        label='宛先', required=False,
        queryset=User.objects.filter(is_active=True).all(),
        # initial = User.objects.filter(is_active=True).values_list('id',flat=True),
        widget=CustomCheckboxSelectMultiple  # ここで、今作ったウィジェットを指定
    )

    # 添付ファイル3つ
    pdf_file1 = forms.FileField(required=False)
    pdf_file2 = forms.FileField(required=False)
    pdf_file3 = forms.FileField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # tags(通知)を横並び
        self.fields['tags'].initial = User.objects.filter(is_active=True).values_list('id',flat=True)

        for field in self.fields.values():
            if 'class' in field.widget.attrs:
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Information
        # fields = ['category', 'title', 'body', 'to_flag', 'filefield'] #'__all__'
        # fields = ['category', 'title', 'body']
        fields = ['title', 'body', 'for_search']
        widgets = {
            # 'body': SummernoteWidget(),
            'body': TinyMCE,   #追加
            'title': forms.TextInput(attrs={'placeholder': 'タイトルを入力してください'}),
            'for_search': forms.TextInput(attrs={'placeholder': '検索キーワード'}),
            # 'is_draft': forms.CheckboxInput(attrs={'class':''}),
        }

        #↑のフィールドのラッピングやめて、ここにカテゴリ等1つずつ書く

#検索
class SearchForm(forms.Form):
        # keyword = forms.CharField(label='検索', max_length=100)
        keyword = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'おしらせの検索', 'class':'form-control bg-white border-0 small', 'type':'search'}))


#コメント入力用
class InfoCommentsForm(forms.ModelForm):
    class Meta:
        model = InfoComments
        fields = ('comment',)


#変更・更新は別で用意か・・
class InformationEditForm(LoginRequiredMixin, forms.ModelForm):

    ## クラス変数として宣言だけしておく。
    # tags = None
    tags = forms.ModelMultipleChoiceField(
        label='宛先', required=False,
        queryset=User.objects.filter(is_active=True).all(),
        # initial = User.objects.filter(is_active=True).values_list('id',flat=True),
        widget=CustomCheckboxSelectMultiple  # ここで、今作ったウィジェットを指定
    )

    # 添付ファイル3つ
    pdf_file1 = forms.FileField(required=False)
    pdf_file2 = forms.FileField(required=False)
    pdf_file3 = forms.FileField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # tags(通知)を横並び
        # lst = User.objects.filter(is_active=True).values_list('id',flat=True)
        self.fields['tags'].initial = User.objects.filter(is_active=True).values_list('id',flat=True)

        # tags = forms.ModelMultipleChoiceField(
        #     label='宛先', queryset=User.objects.filter(is_active=True).all(), required=False,
        #     widget=CustomCheckboxSelectMultiple,  # ここで、今作ったウィジェットを指定
        #     # initial = lst,
        # )

        for field in self.fields.values():
            if 'class' in field.widget.attrs:
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Information
        # fields = ['category', 'title', 'body', 'to_flag', 'filefield'] #'__all__'
        # fields = ['category', 'title', 'body', 'is_draft']
        fields = ['title', 'body', 'is_draft', 'for_search']
        widgets = {
            # 'body': SummernoteWidget(),
            'body': TinyMCE,   #追加
            'for_search': forms.TextInput(attrs={'placeholder': '検索キーワード'}),
        }

        #↑のフィールドのラッピングやめて、ここにカテゴリ等1つずつ書く


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    pdf_file = forms.FileField()


#FAQ検索
class FaqSearchForm(forms.Form):
        keyword = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'FAQの検索', 'class':'form-control bg-white border-0 small', 'type':'search'}))


#全体検索→HTML記述で未使用に。
# class AllSearchForm(forms.Form):
#         all_search_keyword = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'Search for...', 'class':'form-control bg-light border-0 small'}))


#個人ノート検索
class NoteSearchForm(forms.Form):
        keyword = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'ノートの検索', 'class':'form-control bg-white border-0 small', 'type':'search'}))


#ノート登録
class NoteCreateForm(LoginRequiredMixin, forms.ModelForm):

    share = forms.ModelMultipleChoiceField(
        queryset=User.objects.filter(is_active=True).order_by('id'),
        widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(NoteCreateForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['share'].required = False

    class Meta:
        model = Note
        fields = ['title', 'body', 'share', 'for_search']
        widgets = {
            'body': TinyMCE,   #追加
            'title': forms.TextInput(attrs={'placeholder': 'タイトルを入力してください', 'class':'form-control'}),
            'for_search': forms.TextInput(attrs={'placeholder': '検索キーワード', 'class':'form-control'}),
        }

#FAX当番登録
class FaxCreateForm(LoginRequiredMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].initial = date.today()+ relativedelta(days=+1)

    class Meta:
        model = Fax
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type':'date'}),
            'html': forms.Textarea(attrs={'class':'d-none'}),#非表示にするクラス追加
        }