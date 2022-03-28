from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.http import HttpResponse, Http404 # 追記

from django.views import generic
from .models import DailyReport, ReadStates
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

from .forms import InformationForm, FileFormset, InfoCommentsForm, InformationEditForm

from django.contrib import messages
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

            if 'pdf_file1' in request.FILES:
                instance = Attachments(file_path=request.FILES['pdf_file1'] , information=obj)
                instance.save()

            if 'pdf_file2' in request.FILES:
                instance = Attachments(file_path=request.FILES['pdf_file2'] , information=obj)
                instance.save()

            return redirect('myinfo:index')

    else:
        form = InformationForm

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
    read_states = information.info_read.all()
    
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

            request.session['form_data'] = request.POST

            messages.success(request, '更新しました！')
            return redirect('myinfo:detail', pk=pk)

    else:

        form = InformationEditForm(instance=information)

        context ={
            'form': form,
            'information':information,
        }

    return render(request, 'myinfo/edit_fbvform.html', context)
    

#使用中のidndex
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import SearchForm
from django.db.models import Q
def report_list(request):

    #検索
    searchForm = SearchForm(request.GET)

    context = {
        'searchForm': searchForm,
    }

    if searchForm.is_valid():
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
        reports = DailyReport.objects.all().order_by('-id')
        page_obj = paginate_queryset(request, reports, 10)#ページネーション用
        context['page_obj'] = page_obj
        context['informations'] = page_obj.object_list


    #通知（有無だけ）
    if request.user.id is not None:
        notifi_exis =  Notifications.objects.filter(user=request.user).exists()

        context['notifi_exis'] = notifi_exis

    return render(request, 'myreport/report_list.html', context)


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
