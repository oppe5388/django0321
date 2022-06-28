from django.shortcuts import render


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

def new01_02(request):
    return render(request, 'myprofit/new01_02.html')

def new02_02(request):
    return render(request, 'myprofit/new02_02.html')

def new03_02(request):
    return render(request, 'myprofit/new03_02.html')

def new04_02(request):
    return render(request, 'myprofit/new04_02.html')

def new01_03(request):
    return render(request, 'myprofit/new01_03.html')

def new02_03(request):
    return render(request, 'myprofit/new02_03.html')

def new04_03(request):
    return render(request, 'myprofit/new04_03.html')