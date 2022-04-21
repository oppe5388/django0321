from django import forms
from .models import Information, Attachments, InfoComments

from django_summernote.widgets import SummernoteWidget
from django.contrib.auth.mixins import LoginRequiredMixin

# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
from accounts.models import User


from .widgets import CustomCheckboxSelectMultiple
from .widgets import AccordionCheckbox

from tinymce.widgets import TinyMCE  #追加

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
        fields = ['category', 'title', 'body']
        widgets = {
            # 'body': SummernoteWidget(),
            'body': TinyMCE,   #追加
            'title': forms.TextInput(attrs={'placeholder': 'タイトルを入力してください'}),
            # 'is_draft': forms.CheckboxInput(attrs={'class':''}),
        }

        #↑のフィールドのラッピングやめて、ここにカテゴリ等1つずつ書く

#検索
class SearchForm(forms.Form):
        # keyword = forms.CharField(label='検索', max_length=100)
        keyword = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'おしらせの検索', 'class':'form-control bg-white border-0 small'}))


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
        fields = ['category', 'title', 'body', 'is_draft']
        widgets = {
            # 'body': SummernoteWidget(),
            'body': TinyMCE,   #追加
        }

        #↑のフィールドのラッピングやめて、ここにカテゴリ等1つずつ書く


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    pdf_file = forms.FileField()


#FAQ検索
class FaqSearchForm(forms.Form):
        keyword = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'FAQの検索', 'class':'form-control bg-white border-0 small'}))


#全体検索→HTML記述で未使用に。
# class AllSearchForm(forms.Form):
#         all_search_keyword = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'Search for...', 'class':'form-control bg-light border-0 small'}))