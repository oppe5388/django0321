from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.http import HttpResponse, Http404

from .models import DailyReport, CheckStates, ReportRead
from .forms import DailyReportForm, SearchForm #,DailyReportEditForm, 

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from django.contrib import messages
from accounts.models import User

from django.utils import timezone

from django.contrib.auth.decorators import login_required

#LDへへブラウザ通知
from myinfo.models import OneSignalUser
from django.shortcuts import resolve_url
from django.shortcuts import get_list_or_404

#Create
@login_required
def add_fbvform(request):
    if request.method == "POST":
        form = DailyReportForm(request.POST)

        if form.is_valid(): 
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()

            #ReportReadに追加
            for num in range(1, 5):
                user_instance = get_object_or_404(User, pk=num)
                ReportRead.objects.get_or_create(user=user_instance, report=obj)

                #LDへ通知を作る
                # onesignals = get_list_or_404(OneSignalUser, user=num)
                onesignals = OneSignalUser.objects.filter(user=num)
                if onesignals:
                    for one in onesignals:
                        OneSignalUser.push(one,title='日報が作成されました', text=str(obj.day), url=resolve_url('myreport:index'))

            return redirect('myreport:index')

    else:
        form = DailyReportForm

    return render(request, 'myreport/add_fbvform.html', {'form': form })


#Update
@login_required
def edit_fbvform(request, pk, *args, **kwargs):

    dailyreport = get_object_or_404(DailyReport, pk=pk)

    if request.method == 'POST':
        form = DailyReportForm(request.POST, instance=dailyreport)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()

            #ReportReadに追加
            for num in range(1, 5):
                user_instance = get_object_or_404(User, pk=num)
                ReportRead.objects.get_or_create(user=user_instance, report=obj)

            #LDチェック済みを削除
            chk_exis = CheckStates.objects.filter(report=obj).exists()
            if chk_exis == True:
                CheckStates.objects.filter(report=obj).delete()

            messages.success(request, '更新しました！')
            return redirect('myreport:detail', pk=pk)

    else:

        form = DailyReportForm(instance=dailyreport)

        context ={
            'form': form,
            'dailyreport':dailyreport,
        }

    # return render(request, 'myreport/edit_fbvform.html', context)
    return render(request, 'myreport/add_fbvform.html', context)


#Detail
@login_required
def detail_fbvform(request, pk):
    template_name = "myreport/report_detail.html"

    try:
        report = DailyReport.objects.get(pk=pk)
    except DailyReport.DoesNotExist:
        raise Http404("DailyReport does not exist")

    context = {
        "report":report,
    }


    context['reportread'] = ReportRead.objects.filter(report=pk)

    return render(request,template_name,context)


#使用中のidndex
@login_required
def report_list(request):

    #検索
    searchForm = SearchForm(request.GET)

    context = {
        'searchForm': searchForm,
    }

    if searchForm.is_valid():
        queryset = DailyReport.objects.all()
        keyword = searchForm.cleaned_data['keyword']
        if keyword:
            keyword = keyword.split()
            for k in keyword:
                queryset = queryset.filter(
                        Q(body1__icontains=k) | 
                        Q(body2__icontains=k) | 
                        Q(body3__icontains=k) | 
                        Q(body4__icontains=k) | 
                        Q(body5__icontains=k) | 
                        Q(body6__icontains=k)
                    ).order_by('-id')#

            context['dailyreports'] = queryset
    else:
        searchForm = SearchForm()
        reports = DailyReport.objects.all().order_by('-id')
        page_obj = paginate_queryset(request, reports, 10)#ページネーション用
        context['page_obj'] = page_obj
        context['dailyreports'] = page_obj.object_list

    check_set = CheckStates.objects.all()
    read_set = ReportRead.objects.all()

    context['check_set'] = check_set
    context['read_set'] = read_set

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


#LDチェックのCreate　＋未読を削除することにした
@login_required
def add_check(request, pk):
    user_instance = request.user
    dailyreport = get_object_or_404(DailyReport, pk=pk)
    # CheckStates.objects.create(user=user_instance, report=dailyreport)
    CheckStates.objects.get_or_create(user=user_instance, report=dailyreport)
    

    #既読にする（中間テーブルから削除する）
    read_exis = ReportRead.objects.filter(user=request.user, report=dailyreport).exists()
    if read_exis == True:
        ReportRead.objects.filter(user=request.user, report=dailyreport).delete()


    # return redirect(request.META['HTTP_REFERER'])#元のページに戻る
    return redirect('/myreport/')
