from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import MoneyTrans
from .forms import MoneyForm
from datetime import date, datetime, timedelta
from django.contrib import messages

from django.conf import settings
from django.http import JsonResponse

#長得の月計算用
from dateutil.relativedelta import relativedelta

# 未着リスト用
import jpbizday
from myinfo.models import Holiday


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



def next_bizday_calc(target_day):
    # 次の平日を取得、VCC休業日は祝日と同じ扱い
    # while jpbizday.is_bizday(mail_date) == False \
    #     or Holiday.objects.filter(title="1", non_date=mail_date).exists() \
    #     or Holiday.objects.filter(title="2", non_date=mail_date).exists():

    while jpbizday.is_bizday(target_day) == False:
        target_day = target_day + timedelta(1)
    
    return target_day


def fifth_bizday_calc(target_year, target_month):
    bizdays = jpbizday.month_bizdays(target_year, target_month)
    
    # 2次休業日に登録されている日はリストから削除する
    for data in Holiday.objects.filter(title="4"):
        if data.non_date in bizdays:
            bizdays.remove(data.non_date)
    
    fifth_bizday = bizdays[4]
    return fifth_bizday


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
    list_set = [] 
    for i in range(5):
        base_day = date.today() + relativedelta(months= i-2)#-2ヶ月から+2ヶ月の5ヶ月間
        start_year = int(base_day.strftime("%Y"))
        start_month = int(base_day.strftime("%m"))
        
        list = [] 
        
        #5営業日目
        mail_send_day = fifth_bizday_calc(start_year, start_month)
        list.append(mail_send_day)
        #対象月
        target_term1 = (base_day - relativedelta(months=4)).strftime("%-m")+'月'
        target_term2 = (base_day - relativedelta(months=3)).strftime("%-m")+'月'
        target_term3 = (base_day - relativedelta(months=2)).strftime("%-m")+'月'
        list.append(target_term1 +"・"+ target_term2 +"・"+ target_term3)
        #前月10日（土日祝は翌日）
        mail_deadline = next_bizday_calc(base_day + relativedelta(months=-1,day=10,))
        list.append(mail_deadline)
        #前月末
        mail_pickup = base_day + relativedelta(months=0,day=1,days=-1)
        list.append(mail_pickup)
        
        list_set.append(list)
        context['list' + str(i+1)] = list
    
    context['list_set'] = list_set

    return render(request, "mysched/mysched.html", context)


    # Model.objects.filter(field__gt='value') #大きい場合
    # model.objects.filter(field__gte='value') #以上の場合
    # Model.objects.filter(field__lt='value') #未満の場合
    # model.objects.filter(field__lte='value') #以下の場合
