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

    #登録日をカレンダーで選択→表示用
    if moneyForm.is_valid():
        input_date = moneyForm.cleaned_data['input_date']
        # request.session['form_data'] = request.GET
        
        if input_date:
            #入力日以降のクエリセットの1つ目
            past_sched = MoneyTrans.objects.filter(entry__gte=input_date).order_by('entry').first()
            context['past_sched'] = past_sched
            context['input_date'] = input_date

    return render(request, "mysched/mysched.html", context)


    # Model.objects.filter(field__gt='value') #大きい場合
    # model.objects.filter(field__gte='value') #以上の場合
    # Model.objects.filter(field__lt='value') #未満の場合
    # model.objects.filter(field__lte='value') #以下の場合