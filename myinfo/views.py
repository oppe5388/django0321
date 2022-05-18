from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.http import HttpResponse, Http404

from django.views import generic
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

from .forms import *

from django.contrib import messages

# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
from accounts.models import User

from django.utils import timezone
import os

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from django_datatables_view.base_datatable_view import BaseDatatableView
# from ajax_datatable.views import AjaxDatatableView

from django.conf import settings
from django.http import JsonResponse

import operator


#Ajaxで未読削除
def ajax_read_delete(request, pk, *args, **kwargs):
    if request.is_ajax():
        ReadStates.objects.filter(user=request.user, information=pk).delete()
        return JsonResponse({"message":"success"})


#関数ビューで通知の中間テーブルCreateを作ってみる
def add_fbvform(request):
    if request.method == "POST":
        form = InformationForm(request.POST, request.FILES)

        if form.is_valid(): 
            obj = form.save(commit=False)
            obj.user = request.user
            obj.created_at = timezone.datetime.now()
            obj.updated_at = timezone.datetime.now()

            #下書きチェックだったら
            if request.POST.get('draft') is not None: 
                obj.is_draft = True
            obj.save()

            #添付ファイル：保存＆モデル書き込み
            # pdf_files = request.FILES.getlist()
            # for pdf in pdf_files:
            if 'pdf_file1' in request.FILES:
                instance = Attachments(file_path=request.FILES['pdf_file1'] , information=obj)
                instance.save()

            if 'pdf_file2' in request.FILES:
                instance = Attachments(file_path=request.FILES['pdf_file2'] , information=obj)
                instance.save()

            if 'pdf_file3' in request.FILES:
                instance = Attachments(file_path=request.FILES['pdf_file3'] , information=obj)
                instance.save()

            # user = get_object_or_404(User, pk=request.POST["notification_user"])#これで出来た
            # user = User.objects.get(pk=request.POST["notification_user"])
            # Notifications.objects.create(user=user, information=obj)

            #通知：選択したユーザー
            result = request.POST.getlist("tags")
            for user in result:
                # user_instance = User.objects.get(pk=user)#これ出来ない・
                user_instance = get_object_or_404(User, pk=user)
                # Notifications.objects.create(user=user_instance, information=obj)
                #既読も同じでok？
                ReadStates.objects.create(user=user_instance, information=obj)

            #↓これ↓が最終
            # file = request.FILES.get('file')
            # Attachments.objects.create(file_path=file, information=obj)
            #↓これ↑が最終

                # for file in files:
                #     Attachments.objects.create(file_path=file, information=obj)

            return redirect('myinfo:index')

    else:
        form = InformationForm

        #ここに

    return render(request, 'myinfo/add_fbvform.html', {'form': form })


#Detail関数ビュー
def detail_fbvform(request, pk):
    template_name = "myinfo/information_detail.html"

    try:
        information = Information.objects.get(pk=pk)
    except Information.DoesNotExist:
        raise Http404("Information does not exist")

    #コメント入力時
    if request.method == 'POST':

        # 投稿されたコメントをデータベースに保存
        if request.POST["text"] != "":
            InfoComments.objects.create(
                comment=request.POST["text"],
                information=information,
                user = request.user
                )
        else:
            messages.warning(request, 'コメント欄は未入力です')
    
    #通知表示用（有無だけ）
    if request.user.id is not None:
        notifi_exis =  Notifications.objects.filter(user=request.user).exists()

        context = {
            "information":information,
            'notifi_exis':notifi_exis,
        }

        #既読にする（中間テーブルから削除する）
        read_exis = ReadStates.objects.filter(user=request.user, information=pk).exists()
        if read_exis == True:
            ReadStates.objects.filter(user=request.user, information=pk).delete()

    else:
        context = {
            "information":information,
        }

    return render(request,template_name,context)


#Update関数ビューつくる
def edit_fbvform(request, pk, *args, **kwargs):

    information = get_object_or_404(Information, pk=pk)

    #外部キーなので_set.all()でなくrelated_nameで
    attachments = information.info_attach.all()
    notifications = information.info_notifi.all()
    read_states = information.info_read.all()
    
    if request.method == 'POST':
        form = InformationEditForm(request.POST, request.FILES, instance=information)

        if form.is_valid(): 
            obj = form.save(commit=False)
            obj.user = request.user

            #更新日時も更新するチェックだったら
            if request.POST.get('chk') is not None: 
                obj.updated_at = timezone.datetime.now()

            #下書きチェックだったら
            if request.POST.get('draft') is not None: 
                obj.is_draft = True
            else:
                obj.is_draft = False

            obj.save()

            #添付ファイル3つ
            if 'pdf_file1' in request.FILES:
                instance = Attachments(file_path=request.FILES['pdf_file1'] , information=obj)
                instance.save()
            if 'pdf_file2' in request.FILES:
                instance = Attachments(file_path=request.FILES['pdf_file2'] , information=obj)
                instance.save()
            if 'pdf_file3' in request.FILES:
                instance = Attachments(file_path=request.FILES['pdf_file3'] , information=obj)
                instance.save()

            #全員未読にするチェックだったら
            if request.POST.get('chk2') is not None: 
                #通知：選択したユーザー
                result = request.POST.getlist("tags")
                for user in result:
                    # user_instance = User.objects.get(pk=user)#これ出来ない・
                    user_instance = get_object_or_404(User, pk=user)
                    # Notifications.objects.get_or_create(user=user_instance, information=obj)
                    #既読も
                    ReadStates.objects.get_or_create(user=user_instance, information=obj)


            request.session['form_data'] = request.POST

            messages.success(request, '更新しました！')
            return redirect('myinfo:detail', pk=pk)

        else:
            messages.error(request, '更新できませんでした。内容を確認してください。')
            return redirect('myinfo:update', pk=pk)


    # 一覧表示からの遷移や、確認画面から戻った時
    form = InformationEditForm(instance=information)

    context ={
        'form': form,
        'information':information,
        'notification':notifications,
        'attachment':attachments,
        'read_state':read_states,
        
    }

    return render(request, 'myinfo/edit_fbvform.html', context)


#使用中のidndex
def information_list(request):

    #検索
    #検索結果をページネーションするにはSessionから条件取得？
    #→中止して、検索の場合、ページネーションなしにしよう。  
    searchForm = SearchForm(request.GET)

    context = {
        'searchForm': searchForm,
    }

    if searchForm.is_valid():
        # informations = Information.objects.filter(title__contains=keyword).order_by('-id')#ひとまずタイトルに含む
        # タイトルor本文に含む（複数ワード、区切りは半角でも全角スペースでもOK
        queryset = Information.objects.all()
        keyword = searchForm.cleaned_data['keyword']
        if keyword:
            keyword = keyword.split()
            for k in keyword:
                queryset = queryset.filter(
                        Q(title__icontains=k) | 
                        Q(body__icontains=k)
                    ).order_by('-updated_at')#

            context['informations'] = queryset
    else:
        searchForm = SearchForm()
        informations = Information.objects.all().order_by('-updated_at')
        page_obj = paginate_queryset(request, informations, 20)#ページネーション用
        context['page_obj'] = page_obj
        context['informations'] = page_obj.object_list

    #通知（有無だけ）
    if request.user.id is not None:
        notifi_exis =  Notifications.objects.filter(user=request.user).exists()

        #既読も
        # my_unread = ReadStates.objects.all().filter(user=request.user)
        unread_set = ReadStates.objects.all()

        #contextは辞書型、context['weather'] = '晴れ'、でkeyがweather、valueが晴れというデータを追加
        context['notifi_exis'] = notifi_exis
        context['unread_set'] = unread_set


    return render(request, 'myinfo/information_list.html', context)


#ページネーション
def paginate_queryset(request, queryset, count):
    paginator = Paginator(queryset, count)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return page_obj


class DeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = Information
    success_url = reverse_lazy('myinfo:index')

    def delete(self, request, *args, **kwargs):
        self.object = post = self.get_object()
        message = f'削除しました！'
        post.delete()
        messages.info(self.request, message)
        return redirect(self.get_success_url())


UPLOAD_DIR = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'  # アップロードしたファイルを保存するディレクトリ
#同じファイル名は上書き保存されてしまうけど
def handle_uploaded_file(f):
    path = os.path.join(UPLOAD_DIR, f.name)#これ追記：これで引っ張ってくる
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

#通知削除
def notifi_delete(request):
    Notifications.objects.filter(user=request.user).delete()

    # return redirect('myinfo:index')
    return redirect(request.META['HTTP_REFERER'])#元のページに戻る

#添付削除
def attach_delete(request, pk):
    Attachments.objects.filter(pk=pk).delete()
    return redirect(request.META['HTTP_REFERER'])#元のページに戻る

#listからの既読削除
def read_delete(request, pk):
    #既読にする（中間テーブルから削除する）
    read_exis = ReadStates.objects.filter(user=request.user, information=pk).exists()
    if read_exis == True:
        ReadStates.objects.filter(user=request.user, information=pk).delete()
    return redirect(request.META['HTTP_REFERER'])#元のページに戻る


#シフト表
def shift(request):

    workshifts = WorkShifts.objects.all().order_by('-created_at')
    context = {
        "workshifts":workshifts,
    }

    return render(request, 'myinfo/shift.html', context)


#FAQリスト
def faqs_list(request):

    faqsearchForm = FaqSearchForm(request.GET)

    context = {
        'faqsearchForm': faqsearchForm,
    }
    #ディーラーのall←全部とってくる用
    #窓口のallは使わないか
    #別フィールド作ってTrueFalseで分岐をテンプレートに書く（or紐付いていなかったらallということにするか）
    context['dealers_all'] = Dealers.objects.all().order_by('id')
    context['contacts_all'] = Contacts.objects.all().order_by('id')
    #↓1件でもクエリセットだとtemplateでループ要になるため、firstつける
    context['helpdesk'] = Contacts.objects.filter(name__contains="日産ヘルプデスク").first()

    if faqsearchForm.is_valid():
        queryset = Faqs.objects.all()
        keyword = faqsearchForm.cleaned_data['keyword']
        if keyword:
            keyword = keyword.split()
            for k in keyword:
                queryset = queryset.filter(
                        Q(question__icontains=k) | 
                        Q(answer1__icontains=k) | 
                        Q(answer2__icontains=k) | 
                        Q(reference__icontains=k)
                    ).order_by('-updated_at')#

            context['faqs'] = queryset
            context['selected_tab'] = '検索結果'
    else:
        faqsearchForm = FaqSearchForm()
        faqs = Faqs.objects.all().order_by('-updated_at', 'id')
        page_obj = paginate_queryset(request, faqs, 50)#ページネーション用
        context['page_obj'] = page_obj
        context['faqs'] = page_obj.object_list
        context['selected_tab'] = 'すべて'


    return render(request, 'myinfo/faqs.html', context)


#FAQタブ、共通化で作れるか
def faqs_tab(request, p):

    faqsearchForm = FaqSearchForm(request.GET)

    context = {
        'faqsearchForm': faqsearchForm,
    }

    context['dealers_all'] = Dealers.objects.all().order_by('id')
    context['contacts_all'] = Contacts.objects.all().order_by('id')
    #↓1件でもクエリセットだとtemplateでループ要になるため、firstつける
    context['helpdesk'] = Contacts.objects.filter(name__contains="日産ヘルプデスク").first()

    # 一度queryset = Faqs.objects.all()と刻む必要はない
    queryset = Faqs.objects.filter(
                Q(reference__icontains=p)
            ).order_by('-updated_at')
    context['selected_tab'] = p
    context['faqs'] = queryset

    return render(request, 'myinfo/faqs.html', context)



#FAQ Datatablesバージョン
class FaqsJsonView(BaseDatatableView):
    # モデルの指定
    model = Faqs
    # 表示するフィールドの指定
    columns = ['id', 'question', 'answer1', 'answer2', 'reference']


    def filter_queryset(self, qs):

        search = self.request.GET.get('search[value]', None)
        if search:
            search_parts = search.split()
            for part in search_parts:
                qs = qs.filter(
                        Q(question__icontains=part) | 
                        Q(answer1__icontains=part) | 
                        Q(answer2__icontains=part) | 
                        Q(reference__icontains=part)
                    )
        return qs


#全体検索
def all_search(request):

    keyword = request.GET.get('all_search')
    context = {
        'keyword': keyword,
    }

    context['dealers_all'] = Dealers.objects.all().order_by('id')
    context['contacts_all'] = Contacts.objects.all().order_by('id')
    #↓1件でもクエリセットだとtemplateでループ要になるため、firstつける
    context['helpdesk'] = Contacts.objects.filter(name__contains="日産ヘルプデスク").first()

    #おしらせの検索ここに
    queryset = Information.objects.all()
    if keyword:
        keyword = keyword.split()
        for k in keyword:
            queryset = queryset.filter(
                    Q(title__icontains=k) | 
                    Q(body__icontains=k)
                ).order_by('-updated_at')#

        # context = {
        #     'informations': queryset,
        # }
        context['informations'] = queryset


    #FAQ
    queryset = Faqs.objects.all()
    keyword = request.GET.get('all_search')
    if keyword:
        keyword = keyword.split()
        for k in keyword:
            queryset = queryset.filter(
                    Q(question__icontains=k) | 
                    Q(answer1__icontains=k) | 
                    Q(answer2__icontains=k) | 
                    Q(reference__icontains=k)
                ).order_by('-updated_at')#

        context['faqs'] = queryset

    #窓口
    queryset = Contacts.objects.all()
    keyword = request.GET.get('all_search')
    if keyword:
        keyword = keyword.split()
        for k in keyword:
            queryset = queryset.filter(
                    Q(name__icontains=k) | 
                    Q(title__icontains=k) | 
                    Q(job__icontains=k) | 
                    Q(tel__icontains=k) | 
                    Q(searchwords__icontains=k)
                ).order_by('id')#

        context['contacts'] = queryset

    return render(request, 'myinfo/search_result.html', context)



class ContactsJsonView(BaseDatatableView):
    # モデルの指定
    model = Contacts
    # 表示するフィールドの指定
    columns = ['id', 'incoming', 'name', 'tel', 'hours', 'title', 'job', 'searchwords', 'attachments']

    # column_defs = [
    #     {
    #         'name': 'id',
    #         'visible': False,
    #     }, {
    #         'name': 'incoming',
    #     }, {
    #         'name': 'name',
    #     }, {
    #         'name': 'tel',
    #     }, {
    #         'name': 'hours',
    #     }, {
    #         'name': 'title',
    #     }, {
    #         'name': 'job',
    #     }, {
    #         'name': 'searchwords',
    #     }, {
    #         'name': 'attachments',
    #     }
    # ]
    # ↓ManyToManyができない
    # def get_initial_queryset(self, request=None):
    #     # Optimization: Reduce the number of queries due to ManyToMany "tags" relation
    #     return Attachments.objects.prefetch_related('file_path')
    #     # return Attachments.objects.all().prefetch_related('file_path')

    # def customize_row(self, row, obj):
    #     # 'row' is a dictionary representing the current row, and 'obj' is the current object.
    #     # Display tags as a list of strings
    #     # row['attachments'] = ','.join( [t.file_path for t in obj.attachments.all()])
    #     # row['attachments'] = ','.join( [t for t in obj.attachments.all()])
    #     row['attachments'] = "あいうえお"
    #     return

    
    # # ↓FKeyでやってみる
    # def render_column(self, row, column):
    #     if column == 'attachments':
    #         if ContactAttachRel.objects.filter(contact=row.id).exists():
    #             cont =ContactAttachRel.objects.filter(contact=row.id).first()
    #             return cont.attachment.file_path.url
    #             # return "添付あり"
    #         else:
    #             return "ああ"
    #     else:
    #         return super(ContactsJsonView, self).render_column(row, column)


    # # 検索方法の指定：部分一致
    # def get_filter_method(self):
    #     return super().FILTER_ICONTAINS


    def filter_queryset(self, qs):

        search = self.request.GET.get('search[value]', None)
        if search:
            search_parts = search.split()
            for part in search_parts:
                qs = qs.filter(
                        Q(incoming__icontains=part) | 
                        Q(name__icontains=part) | 
                        Q(title__icontains=part) | 
                        Q(job__icontains=part) | 
                        Q(tel__icontains=part) | 
                        Q(hours__icontains=part) | 
                        Q(searchwords__icontains=part)
                    )
        return qs


class DealersJsonView(BaseDatatableView):
    # モデルの指定
    model = Dealers
    # 表示するフィールドの指定
    columns = ['id', 'code5', 'code4', 'name', 'full_name', 'domain', 'customer_desk',	'emergency', 'bc', 'nfs', 'in_house', 'base', 'base_tel']

    # 検索方法の指定：ワード1つならこれだけでOK
    def get_filter_method(self):
        return super().FILTER_ICONTAINS


class ShopsJsonView(BaseDatatableView):
    model = Shops
    # columns = ['id', 'dealer', 'name', 'shopcode', 'tel', 'fax', 'homepage', 'memo', 'kana']
    # ↓でソートはOKでも、検索でエラー
    columns = [
        'id',
        'dealer__name',
        'name',
        'shopcode',
        'tel',
        'fax',
        'homepage',
        'memo',
        'kana',
        'dealer__pk',
        'dealer__code5',
        'dealer__code4',
        'dealer__full_name',
        'dealer__domain',
        'dealer__customer_desk',
        'dealer__emergency',
        'dealer__bc',
        'dealer__nfs',
        'dealer__in_house',
        'dealer__base',
        'dealer__base_tel',
        ]
    def render_column(self, row, column):
        if column == 'dealer__name':
            return row.dealer.name
            # return row.dealer.pk #pkも返せる
        elif column == 'dealer__pk':
            return row.dealer.pk
        elif column == 'dealer__code5':
            return row.dealer.code5
        elif column == 'dealer__code4':
            return row.dealer.code4
        elif column == 'dealer__full_name':
            return row.dealer.full_name
        elif column == 'dealer__domain':
            return row.dealer.domain
        elif column == 'dealer__customer_desk':
            return row.dealer.customer_desk
        elif column == 'dealer__emergency':
            return row.dealer.emergency
        elif column == 'dealer__bc':
            return row.dealer.bc
        elif column == 'dealer__nfs':
            return row.dealer.nfs
        elif column == 'dealer__in_house':
            return row.dealer.in_house
        elif column == 'dealer__base':
            return row.dealer.base
        elif column == 'dealer__base_tel':
            return row.dealer.base_tel
        else:
            return super(ShopsJsonView, self).render_column(row, column)

    # https://pypi.org/project/django-datatables-view/1.20.0/
    # 動作OK
    # def render_column(self, row, column):
    #     if column == 'custom':
    #         return f'{row.dealer}'
    #     else:
    #         return super(ShopsJsonView, self).render_column(row, column)

    # 複数ワード
    def filter_queryset(self, qs):

        search = self.request.GET.get('search[value]', None)
        if search:
            search_parts = search.split()
            for part in search_parts:
                #外部キー検索できる？
                # query = reduce(operator.and_, [ Q(dealer__name__icontains=part) for part in qs ] )
                # qs = qs.filter( query )

                qs = qs.filter(
                        # Q(dealer__icontains=part) | #これがあるとエラーになる
                        Q(dealer__name__icontains=part) | #これでOK
                        Q(name__icontains=part) | 
                        Q(shopcode__icontains=part) | 
                        Q(tel__icontains=part) | 
                        Q(fax__icontains=part) | 
                        Q(homepage__icontains=part) | 
                        Q(memo__icontains=part) | 
                        Q(kana__icontains=part)
                    )
        return qs

# django-ajax-datatable中止
# def contacts(request):
#     return render(request, 'myinfo/contacts_list.html', {})