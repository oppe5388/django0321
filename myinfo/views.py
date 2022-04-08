from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.http import HttpResponse, Http404 # 追記

from django.views import generic
from .models import Information, InfoCategory, Attachments, Notifications, ReadStates, InfoComments
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

from .forms import InformationForm, FileFormset, InfoCommentsForm, InformationEditForm

from django.contrib import messages

# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
from accounts.models import User



from django.utils import timezone


#関数ビューで通知の中間テーブルCreateを作ってみる
def add_fbvform(request):
    if request.method == "POST":
        form = InformationForm(request.POST, request.FILES)

        if form.is_valid(): 
            obj = form.save(commit=False)
            obj.user = request.user
            obj.created_at = timezone.datetime.now()
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
        # form = InfoCommentsForm(request.POST)  # POSTデータをフォームに保存する→これ出来ない
        # if form.is_valid():
        #     comment_obj = form.save(commit=False)
        #     comment_obj.user = request.user
        #     comment_obj.information = information
        #     comment_obj.save()

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

    #添付と通知と既読を取得
    # attachments = Attachments.objects.filter(information_id__exact=pk).all()
    # notifications = Notifications.objects.filter(information_id__exact=pk).all()
    # readStates = ReadStates.objects.filter(information_id__exact=pk).all()

    #外部キーなので_set.all()でなくrelated_nameで
    attachments = information.info_attach.all()
    notifications = information.info_notifi.all()
    read_states = information.info_read.all()

    # unread_member = read_states.values_list('user', flat=True)
    # notifi_member = notifications.values_list('user', flat=True)
    # # read_member = notifi_member.difference(unread_member)

    # read_lst = []


    
    if request.method == 'POST':
        form = InformationEditForm(request.POST, request.FILES, instance=information)

        if form.is_valid(): 
            obj = form.save(commit=False)
            obj.user = request.user
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

            #通知：選択したユーザー
            result = request.POST.getlist("tags")
            for user in result:
                # user_instance = User.objects.get(pk=user)#これ出来ない・
                user_instance = get_object_or_404(User, pk=user)
                Notifications.objects.get_or_create(user=user_instance, information=obj)
                #既読も
                ReadStates.objects.get_or_create(user=user_instance, information=obj)


            request.session['form_data'] = request.POST

            messages.success(request, '更新しました！')
            return redirect('myinfo:detail', pk=pk)

    else:
    # 一覧表示からの遷移や、確認画面から戻った時

        # # セッションにデータがあればそれを使う →tagsリスト入れてとforms.errorが出る
        # if 'form_data' in request.session:
        #     form = InformationEditForm(request.session.get('form_data'))
        # else:
        #     form = InformationEditForm(instance=information)

        form = InformationEditForm(instance=information)

        context ={
            'form': form,
            'information':information,
            'notification':notifications,
            'attachment':attachments,
            'read_state':read_states,
            
        }

    return render(request, 'myinfo/edit_fbvform.html', context)
    



#インラインフォームセットでattachmentモデルに登録
def add_post(request):
    form = InformationForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST' and form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        formset = FileFormset(request.POST, files=request.FILES, instance=post)  # 今回はファイルなのでrequest.FILESが必要
        if formset.is_valid():
            post.save()
            formset.save()
            messages.success(request, '登録しました！')
            return redirect('myinfo:index')

        # エラーメッセージつきのformsetをテンプレートへ渡すため、contextに格納
        else:
            context['formset'] = formset

    # GETのとき
    else:
        # 空のformsetをテンプレートへ渡す
        context['formset'] = FileFormset()

    return render(request, 'myinfo/add_postform.html', context)


#インラインフォームセットのUpdateView
def update_post(request, pk):
    post = get_object_or_404(Information, pk=pk)
    form = InformationForm(request.POST or None, instance=post)
    formset = FileFormset(request.POST or None, files=request.FILES or None, instance=post)
    if request.method == 'POST' and form.is_valid() and formset.is_valid():
        form.save()
        formset.save()
        messages.success(request, '更新しました！')
        # 編集ページを再度表示→DeatalViewにした
        # return redirect('myinfo:update_post', pk=pk)
        return redirect('myinfo:detail', pk=pk)

    context = {
        'form': form,
        'formset': formset
    }

    return render(request, 'myinfo/update_postform.html', context)


#未使用のindex
class IndexView(generic.ListView):
    model = Information
    paginate_by = 3

    def get_queryset(self):
        return Information.objects.order_by('-created_at')

#使用中のidndex
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import SearchForm
from django.db.models import Q
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
                    ).order_by('-id')#

            context['informations'] = queryset
    else:
        searchForm = SearchForm()
        informations = Information.objects.all().order_by('-id')
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


# class DetailView(generic.DetailView):
#     model = Information

# class CreateView(LoginRequiredMixin, generic.edit.CreateView):
#     model = Information
#     # fields = ['category', 'title', 'body', 'to_flag'] #'__all__'
#     form_class = InformationForm

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         messages.success(self.request, "作成しました")
#         return super(CreateView, self).form_valid(form)


# class UpdateView(LoginRequiredMixin, generic.edit.UpdateView):
#     model = Information
#     # fields = ['category', 'title', 'body', 'to_flag'] #'__all__'
#     form_class = InformationForm

#     def dispatch(self, request, *args, **kwargs):
#         obj =self.get_object()
#         if obj.user != self.request.user:
#             raise PermissionDenied('You do not have permission to edit.')
#         return super(UpdateView, self).dispatch(request, *args, **kwargs)

class DeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = Information
    success_url = reverse_lazy('myinfo:index')

    def delete(self, request, *args, **kwargs):
        self.object = post = self.get_object()
        message = f'削除しました！'
        post.delete()
        messages.info(self.request, message)
        return redirect(self.get_success_url())


#使わないけど、テスト
from django.views.generic.edit import FormView
from . import forms
class aaa(generic.edit.FormView):
    form_class = forms.TextForm
    template_name = "formview_test.html"

    # フォームの入力にエラーが無かった場合に呼ばれます
    def form_valid(self, form):
        # form.cleaned_dataにフォームの入力内容が入っています
        data = form.cleaned_data
        text = data["text"]
        search = data["search"]
        replace = data["replace"]
        
        # ここで変換
        new_text = text.replace(search, replace)
        
        # テンプレートに渡す
        ctxt = self.get_context_data(new_text=new_text, form=form)
        return self.render_to_response(ctxt)


import csv
import io
def post_export(request):
    # response = HttpResponse(content_type='text/csv')
    response = HttpResponse(content_type='text/csv; charset=CP932')#Excelで開く用
    response['Content-Disposition'] = 'attachment; filename="posts.csv"'
    # HttpResponseオブジェクトはファイルっぽいオブジェクトなので、csv.writerにそのまま渡せます。
    writer = csv.writer(response)
    for information in Information.objects.all():
        # writer.writerow([information.pk, information.title])
        writer.writerow([
            information.pk,
            information.user,
            information.category,
            information.title,
            information.body,
            information.created_at
            ])
    return response


import os
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

# #コメント投稿
# def comment_post(request, pk):
#     form = InfoCommentsForm(request.POST)
#     if form.is_valid():
#         comment_obj = form.save(commit=False)
#         comment_obj.user = request.user
#         comment_obj.information = information.pk
#         comment_obj.save()

#     return redirect(request.META['HTTP_REFERER'])#元のページに戻る