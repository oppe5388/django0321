from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import MoneyTrans
from .forms import MoneyForm
from datetime import date, datetime


def mysched(request):
    moneyForm = MoneyForm(request.GET)

    # #GETの日付を取得
    # try:
    #     input_date = request.GET["input_date"]

    #     # フォームを規定値で初期化（取得した日付を表示用に入れる）
    #     moneyForm = MoneyForm(initial={
    #         'input_date': input_date,
    #     })
    # except:
    #     pass

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

    #登録日をカレンダーで選択→表示用
    if moneyForm.is_valid():
        input_date = moneyForm.cleaned_data['input_date']

        # if input_date:
        if input_date >= first_date:
            #entryが入力日以降のクエリセットの1つ目
            past_sched = MoneyTrans.objects.filter(entry__gte=input_date).order_by('entry').first()
            context['past_sched'] = past_sched
            context['input_date'] = input_date

            #setoffが入力日以降のクエリセットの1つ目
            setoff_sched = MoneyTrans.objects.filter(setoff__gte=input_date).order_by('entry').first()
            context['setoff_sched'] = setoff_sched

    return render(request, "mysched/mysched.html", context)


    # Model.objects.filter(field__gt='value') #大きい場合
    # model.objects.filter(field__gte='value') #以上の場合
    # Model.objects.filter(field__lt='value') #未満の場合
    # model.objects.filter(field__lte='value') #以下の場合