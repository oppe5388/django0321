from django.shortcuts import render
from .forms import *

def used02(request):
    context = {
        'route': request.GET.get('route'),
    }
    return render(request, 'myprofit/used02.html', context)

def used03(request):
    context = {
        'route': request.GET.get('route'),
    }
    return render(request, 'myprofit/used03.html', context)

def used04(request):
    context = {
        'route': request.GET.get('route'),
        'cert_no': request.GET.get('cert_no'),
        'cancel_flag': request.GET.get('cancel_flag'),
    }
    return render(request, 'myprofit/used04.html', context)

def used05(request):
    context = {
        'route': request.GET.get('route'),
    }
    return render(request, 'myprofit/used05.html', context)

def used06(request):
    #会員証番号欄→これも未使用なのでcontext = {}で良さそう
    searchForm = SearchForm(request.GET)
    context = {
        'searchForm': searchForm,
        'route': request.GET.get('route'),
    }
    return render(request, 'myprofit/used06.html', context)

def used07(request):
    context = {
        'route': request.GET.get('route'),
        'cert_no': request.GET.get('cert_no'),
        'cancel_flag': request.GET.get('cancel_flag'),
    }
    return render(request, 'myprofit/used07.html', context)

def history(request):
    return render(request, 'myprofit/history.html')
    

def profit_top(request):
    context ={'aaa': ''}
    return render(request, 'myprofit/top.html', context)

def new01(request):
    return render(request, 'myprofit/new01.html')

def new02(request):
    return render(request, 'myprofit/new02.html')

def new03(request):
    return render(request, 'myprofit/new03.html')

def new04(request):
    return render(request, 'myprofit/new04.html')

def new05(request):
    return render(request, 'myprofit/new05.html')

def new06(request):
    return render(request, 'myprofit/new06.html')

def new07(request):
    return render(request, 'myprofit/new07.html')

def new08(request):
    return render(request, 'myprofit/new08.html')

def new01_02(request):
    return render(request, 'myprofit/new01_02.html')

def new02_02(request):
    return render(request, 'myprofit/new02_02.html')

def new03_02(request):
    return render(request, 'myprofit/new03_02.html')

def new04_02(request):
    return render(request, 'myprofit/new04_02.html')

def new07_02(request):
    return render(request, 'myprofit/new07_02.html')

def new01_03(request):
    return render(request, 'myprofit/new01_03.html')

def new02_03(request):
    return render(request, 'myprofit/new02_03.html')

def new04_03(request):
    return render(request, 'myprofit/new04_03.html')

def new05_03(request):
    return render(request, 'myprofit/new05_03.html')

def new06_03(request):
    return render(request, 'myprofit/new06_03.html')

def new07_03(request):
    return render(request, 'myprofit/new07_03.html')

def service01_01(request):
    return render(request, 'myprofit/service01_01.html')

def service02_01(request):
    return render(request, 'myprofit/service02_01.html')

def service03_01(request):
    return render(request, 'myprofit/service03_01.html')

def service03_02(request):
    return render(request, 'myprofit/service03_02.html')

def service04_01(request):
    return render(request, 'myprofit/service04_01.html')

def service04_03(request):
    return render(request, 'myprofit/service04_03.html')

def service07_01(request):
    return render(request, 'myprofit/service07_01.html')