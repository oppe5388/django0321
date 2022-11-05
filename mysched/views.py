from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import MoneyTrans
from .forms import MoneyForm
from datetime import date, datetime
from django.contrib import messages

from django.conf import settings
from django.http import JsonResponse

#長得の月計算用
from dateutil.relativedelta import relativedelta
# 未着リスト用
import jpbizday


#長得をajaxで更新：あとで。
def chotoku_calc(request):
    today = date.today()
    #ひとまず4年半前を表示してみる
    four_harf_ago = today - relativedelta(months=54)
    first_day = today.replace(day=1)
    context = {
            'today': today,
            'four_harf_ago': four_harf_ago,
        }
    return JsonResponse(context)


#Ajax
def ajax_sched(request):

    #日付選択あり
    if request.GET.get('input_date'):
        input_date = request.GET.get('input_date')
        input_date = datetime.strptime(input_date, '%Y-%m-%d').date()

        context = {
            'input_date': input_date,
        }
    #日付なし
    else:
        context = {
            'input_date': 'インプットなし',
        }
        return JsonResponse(context)

    first_date = MoneyTrans.objects.order_by('entry').first().entry
    last_date = MoneyTrans.objects.order_by('entry').last().entry

    if input_date >= first_date and input_date <= last_date:
        #entryが入力日以降のクエリセットの1つ目
        context['past_fix'] = MoneyTrans.objects.filter(entry__gte=input_date).order_by('entry').first().fix
        context['past_transfer'] = MoneyTrans.objects.filter(entry__gte=input_date).order_by('entry').first().transfer

        #setoffが入力日以降のクエリセットの1つ目
        context['setoff_transfer'] = MoneyTrans.objects.filter(setoff__gte=input_date).order_by('entry').first().transfer

        return JsonResponse(context)

    else:
        # messages.warning(request, '対象外の日付です。')
        context['else'] = 'elseにいっている'
        return JsonResponse(context)



def mysched(request):
    moneyForm = MoneyForm(request.GET)

    context = {
        'moneyForm': moneyForm,
    }

    #到着期日が今日以降のデータすべて表示用
    moneytrans = MoneyTrans.objects.filter(deadline__gte=date.today()).order_by('deadline')
    context['moneytrans'] = moneytrans

    #該当なし対処のため、1つ目の日付取得
    first_set = MoneyTrans.objects.order_by('entry').first()
    first_date = first_set.entry
    context['first_date'] = first_date

    #検索最終日のために、最後の日付取得
    last_set = MoneyTrans.objects.order_by('entry').last()
    last_date = last_set.entry
    context['last_date'] = last_date


    #長得用
    context['four_harf_ago'] = date.today().replace(day=1) - relativedelta(months=54)


    #登録日をカレンダーで選択→表示用
    if moneyForm.is_valid():
        input_date = moneyForm.cleaned_data['input_date']

        # if input_date:
        if input_date >= first_date and input_date <= last_date:
            #entryが入力日以降のクエリセットの1つ目
            past_sched = MoneyTrans.objects.filter(entry__gte=input_date).order_by('entry').first()
            context['past_sched'] = past_sched
            context['input_date'] = input_date

            #setoffが入力日以降のクエリセットの1つ目
            setoff_sched = MoneyTrans.objects.filter(setoff__gte=input_date).order_by('entry').first()
            context['setoff_sched'] = setoff_sched
        else:
            messages.warning(request, '対象外の日付です。')
            
            
            
    # 未着リスト
    mail_send_day = date.today(day=5) #5営業日：未作成
    mail_deadline = mail_send_day + relativedelta(months=-1,day=10,) #前月10日（土日祝は翌日）：未作成
    mail_pickup = mail_send_day + relativedelta(months=-1,day=1,days=-1) #前月末

    

            
    return render(request, "mysched/mysched.html", context)


    # Model.objects.filter(field__gt='value') #大きい場合
    # model.objects.filter(field__gte='value') #以上の場合
    # Model.objects.filter(field__lt='value') #未満の場合
    # model.objects.filter(field__lte='value') #以下の場合
